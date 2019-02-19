import numpy as np
import pandas as pd
import glob
from os.path import splitext, basename
from scipy.stats import linregress
from operator import itemgetter

import matplotlib.pyplot as plt

def replace_and(x):
    """
    if & or &amp; in value, replace it with /
    """
    replace_list = ['&amp;','/amp;','&']
    for i in replace_list:
        if i in x:
            y = x.replace(i, '/')
            break
        else:
            y = x
    return y

def main():


    df = pd.read_csv('../data/section_3/temp_datalab_records_linkedin_company.csv')
    df['as_of_date'] = pd.to_datetime(df.as_of_date)
    df = df.dropna(subset=['industry'])
    df['industry'] = df.industry.apply(lambda x: replace_and(x))

    df = df[df.employees_on_platform!=0]
    df['followers_to_size'] = df.followers_count/df.employees_on_platform

    print('Fig 1. Followers on linked in')
    fig, ax = plt.subplots(figsize=(10,6))
    followers_to_size = []
    for industry, data in df.groupby('industry'):
        industry_sum = data.groupby('as_of_date')[['followers_count', 'employees_on_platform']].sum()
        y = (industry_sum.followers_count/industry_sum.employees_on_platform).tolist()
        followers_to_size.extend(y)
    ax.hist(followers_to_size, color='slateblue', density=True, bins=np.arange(0, 300, 1)) 
    ax.set_ylabel('Probability density')
    ax.set_xlabel('Followers/size ratio')

    plt.savefig('../result/followers_to_size_ratio.png', dpi=300, transparent=True, bbox_inches='tight')

    print('Fig 101. Followers on linked in grouped for the size')
    fig, ((ax1, ax2, ax3)) = plt.subplots(figsize=(15,3), nrows=1, ncols=3)
    c1 = 'darkmagenta'
    ax1.hist(followers_to_size, color=c1, density=True, bins=np.arange(0, 50, 1), label='0-50') 
    ax1.set_ylabel('Probability density')
    ax1.set_xlabel('Followers/size ratio')
    c2 = 'indianred'
    ax2.hist(followers_to_size, color=c2, density=True, bins=np.arange(50, 300, 1), label='50-300') 
    ax2.set_xlabel('Followers/size ratio')
    c3 = 'forestgreen'
    ax3.hist(followers_to_size, color=c3, density=True, bins=np.arange(300, 600, 1), label='300-600') 
    ax3.set_xlabel('Followers/size ratio')

    h1, l1 = ax1.get_legend_handles_labels()
    h2, l2 = ax2.get_legend_handles_labels()
    h3, l3 = ax3.get_legend_handles_labels()

    fig.legend(h1+h2+h3, l1+l2+l3, loc='upper right')
    plt.savefig('../result/followers_to_size_ratio_group.png', dpi=300, transparent=True, bbox_inches='tight')

    print('Fig 2. Changes in followers over time')
    company = input('Put in the industry name e.g. Investment Banking')
    df_test = df[df.industry == company]
    fig, ax = plt.subplots(figsize=(10,6))
    for c, data in df_test.groupby('company_name'):
        ax.scatter(x=data.as_of_date, y=data.followers_count/data.employees_on_platform, label=c, s=5)
    ax.legend(bbox_to_anchor=(1., 1.), markerscale=5)

    ax.set_ylabel('Followers/size ratio')
    ax.set_xlabel('Time')
    plt.savefig('../result/followers_size_over_time_{}.png'.format(company), dpi=300, transparent=True, bbox_inches='tight')
    
if __name__ == '__main__':
    main()
 
