from os.path import abspath
import pandas as pd
import numpy as np
import math
from scipy import stats

def zipcode(x):
    """
    change zip code from float to int
    """
    try:
        y = int(x)
    except ValueError:
        if type(x) == str:
            y = int(x.split('-')[0])
        elif math.isnan(x):
            y = 0
        
    return y 


def main():
    
    # path to each document
    # column description file
    desc_fname = abspath('../data/section_1/OPEN_DATA_FIRE_INCIDENTS_FILE_DESCRIPTION.xls')
    # fire incident data file
    data_fname = abspath('../data/section_1/Incidents_Responded_to_by_Fire_Companies.csv')
    # 2010 census data file name
    census_fname = abspath('../data/section_1/census_zipcode_2010.csv')

    df_desc = pd.read_excel(desc_fname)
    df_data = pd.read_csv(data_fname)
    #translate zip code
    df_data['INCIDENT_TYPE_CODE'] = df_data['INCIDENT_TYPE_DESC'].apply(lambda x: x.split(' - ')[0])
    df_census = pd.read_csv(census_fname)

    print('1. Most common incident: ')
    incidents = pd.DataFrame(df_data.groupby('INCIDENT_TYPE_DESC')['INCIDENT_TYPE_DESC'].size())
    incidents['incident_ratio'] = incidents['INCIDENT_TYPE_DESC']/len(df_data)
    most_common_incident = incidents.sort_values('incident_ratio').incident_ratio.iloc[-1]
    print(most_common_incident)

    print('\n 2. False calls in Staten island vs Manhattan')
    df_false = df_data[df_data['INCIDENT_TYPE_CODE'] == '710']   
    df_false_dest = pd.DataFrame(df_false.groupby('BOROUGH_DESC').size())
    manhattan = df_false_dest[df_false_dest.index == '1 - Manhattan'].values[0][0]
    staten = df_false_dest[df_false_dest.index =='3 - Staten Island'].values[0][0]
    false_ratio = staten/manhattan
    print(false_ratio)

    print('\n 3. Most frequent cooking fire hour ratio')
    df_cooking = df_data[['INCIDENT_TYPE_DESC', 'INCIDENT_TYPE_CODE', 'INCIDENT_DATE_TIME']]
    df_cooking['Hour'] = pd.to_datetime(df_cooking['INCIDENT_DATE_TIME']).dt.hour
    hour_count = df_cooking.groupby('Hour')['INCIDENT_TYPE_CODE'].count()
    cooking_count = df_cooking[df_cooking.INCIDENT_TYPE_CODE == '113'].groupby('Hour')['INCIDENT_TYPE_CODE'].count()
    cooking_proba = pd.DataFrame(cooking_count/hour_count)
    max_cooking_fire = cooking_proba.max()[0]
    print(max_cooking_fire)

    print('\n 4. Average number of units in 111 vs 651')
    df_111_651 = df_data[df_data.INCIDENT_TYPE_CODE.isin(['111', '651'])]
    units_111 = df_111_651.groupby('INCIDENT_TYPE_CODE')['UNITS_ONSCENE'].mean()['111']
    units_651 = df_111_651.groupby('INCIDENT_TYPE_CODE')['UNITS_ONSCENE'].mean()['651']
    unit_ratio = units_111/units_651
    print(unit_ratio)

    print('\n 5. About 111 incidents...')
    df_111 = df_data[df_data.INCIDENT_TYPE_CODE=='111'][['INCIDENT_DATE_TIME', 'ARRIVAL_DATE_TIME', 'ZIP_CODE']].dropna()
    for c in ['INCIDENT_DATE_TIME', 'ARRIVAL_DATE_TIME']:
        df_111[c] = pd.to_datetime(df_111[c])
    print('5-1. 3rd quartile in difference in call and arrival time')
    df_111['min_diff'] = (df_111.ARRIVAL_DATE_TIME - df_111.INCIDENT_DATE_TIME)/np.timedelta64(1, 'm')
    third_quartile = np.percentile(df_111.min_diff.values, 75)
    print(third_quartile)
    print('5-2. R-square for zip code population vs incidents')
    df_zipcode = pd.DataFrame(index=df_111.ZIP_CODE.unique())
    df_census = df_census.set_index('Zip Code ZCTA')
    df_zipcode['incidents'] = df_111.groupby('ZIP_CODE').size()
    df_zipcode = df_zipcode.merge(df_census, left_index=True, right_index=True)
    df_zipcode = df_zipcode.rename(columns={'2010 Census Population': 'population'})
    y = df_zipcode['incidents']
    x = df_zipcode['population']
    slope, intercept, r_value, p_value, std_err = stats.linregress(x, y)
    print(r_value)

    print('\n 6. About CO detectors...')
    df_co = df_data[~df_data.CO_DETECTOR_PRESENT_DESC.isnull()]
    df_co['duration_min'] = pd.to_timedelta(pd.to_timedelta(df_co['TOTAL_INCIDENT_DURATION'], unit='s')/np.timedelta64(1, 'm'), unit='m')
    print('6-1 Incident duration ratios')
    df_co_group = pd.DataFrame(df_co.groupby(['CO_DETECTOR_PRESENT_DESC', pd.TimeGrouper(key='duration_min', freq='10Min')])['duration_min'].size())
    df_co_binned = pd.DataFrame(index=df_co_group.loc['No'].index)
    df_co_binned['no'] = df_co_group.loc['No']/df_co_group.loc['No'].sum()
    df_co_binned['yes'] = df_co_group.loc['Yes']/df_co_group.loc['Yes'].sum()
    df_co_binned['ratio'] = df_co_binned['no']/df_co_binned['yes']
    df_co_binned = df_co_binned.iloc[2:7]
    df_co_binned['mid_bin'] = [25, 35, 45, 55, 65]
    x = df_co_binned.mid_bin
    y = df_co_binned.ratio
    a, b, r, p, stderr = stats.linregress(x, y)
    predicted = a*39+b
    print(predicted)
    print('6-2 Chi square statistics likelihood to be longer')
    df_co['long'] = df_co.duration_min.apply(lambda x: 'long' if x > pd.Timedelta(minutes=60) else 'short')
    df_co.groupby(['CO_DETECTOR_PRESENT_DESC', 'long']).size().unstack()
    df_co_time = df_co.groupby(['CO_DETECTOR_PRESENT_DESC', 'long']).size().unstack()
    statistic, p = stats.chisquare([df_co_time['long']['No']/df_co_time.loc['No'].sum()], [df_co_time['long'].sum()/df_co_time.values.sum()])
    print(statistic)

if __name__ == '__main__':
    main()
 