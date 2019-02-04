# Data Incubator Project Challenge
# Can opinions of the current and potential employees predict performance and growth of a company?

## Project Summary
I propose to build a predictive model relating opinions by the employees and job seekers of a company to the potential growth of the company. Job seekers and employees are the people who are highly interested in the company, therefore their opinions about the company can be sensitive towards the company's performace changes although it may not be apparent. The goal is to see whether these opinions can predict the future of a company. Here, I use reviews and follower data on Glassdoor and LinkedIn as the indicators of opnions and the stock prices and job postings as indicators of the company's performace and growth. 

## Project motivation

As an active job seeker, one of my main criteria in finding the right place to work is the potential to grow. However, with the high volume of available information, and interdiscplinary-ness of the position I am looking for (which is data scientist) can become a full-time job just searching for jobs. I have accumulated more knowledge about companies that hire data scientist during last year than rest of my life. I believe that the point of time when someone is most interested in a company is when they are looking for career opportunities and while they are working. Therefore their opinions would be a good indicator for company's growth. I will se two job boards as sources of opinions from the users, LinkedIn and Glassdoor and use job postings and stock prices as the indicator of their potential growth and performance. 

## Project data
### Opinions data
 - **Linkedin profiles**
 
This database tracks and records the number of employees across companies on daily basis and provides real time insight into how aggressively a company is growing vs its own plans and within its industry.

 - **Glassdoor reviews**
 
The data will consist of reviews on the company fromthe employees and employers.
 
### Performance data

- **Job postings**

This database tracks individual job postings on corporate websites, allowing researchers and data scientists to view overall hiring plans of a company overtime. As well as historical data, users explore in a great detail what types of positions a company is looking to fill, where a company is looking to grow geographically, and in what specific product/business lines the company is looking to expand the most.

- **Stock prices**

This data will consist of stock prices over time for each company

## Preliminary Analysis
### LinkedIn follower trends
As a preliminary analysis I looked at the size of the followers for each company on LinkedIn and normalized for its size. As the estimation of company size, I used the number of employees on LinkedIn. 
The follower size can be divided roughly into 3 groups, 0-50, 50-300 and 300-600. 
Which means the group that has larger follower size is attracting more followers online, which can be an indicator for potential growth

![fig1](https://github.com/hyojunada/data_incubator/blob/master/result/followers_to_size_ratio.png)
![fig1-1](https://github.com/hyojunada/data_incubator/blob/master/result/followers_to_size_ratio_group.png)


Then I looked at the changes in follower size (normalized over company's size) over time for individual companies in each industry
Shown below is the example for Investment Banking industry. From this I can identify which company's gaining more followers and whether it's growing faster or slower than the company norm. In [this notebook](https://github.com/hyojunada/data_incubator/blob/master/notebook/Section3-fig2_increase_of_followers_over_time.ipynb) you can do this for individual companies and see aggregated result for the entire industry. The aggregated result for the entire industry shows how much online interst the industry has compared to its size and whether the interest is growing or not. 

![fig2](https://github.com/hyojunada/data_incubator/blob/master/result/followers_size_over_time_Investment%20Banking.png)

## Next Steps
### Data aquisition and exploration
1. Use Glassdor reviews to measure employees and interviewees' opinions on the companys over time. 
2. Use the Job posting data to measure the expansion of a company as a measure of growth
3. Use the stock prices over time to measure the performance of a company.
## Build predictive model
After elementary analysis reveals an underlying trend that prompts further exploration. For my project I propose to expand these efforts by building a model that takes advantage of the underlying trend in four different data sets. I will combine LinkedIn and Glassdoor data as predictors and Job posting and stock prices as one target variable. The model will allow job seekers to be able to evaluate the potential growth of a company and this can be expanded to other groups of interests such as investorsin when evaluating a company.
