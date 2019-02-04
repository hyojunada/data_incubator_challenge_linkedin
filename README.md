# Data Incubator Project Challenge
# Using company's evaluation and prominence on LinkedIn/Glassdoor to predict their performance

## Project Summary
I propose to build a predictive model relating how people in job seeking position view it as their potential employer to the value of the company in the market. Job seekers and employees are the people who are highly interested in the company, therefore there opinions about the company can be a sensitive predictor of how well the company will do in the future. The goal is to see whether user activities on LinkedIn and Glassdoor can predict the stock prices of the company. I will use NLP to quantify reviews and assortment of factors from LinkedIn and Glassdoor. The stock prices will be used as indicators of the company's performance. 

## Project motivation

As an active job seeker, one of my main criteria in finding the right place to work is the potential to grow. However, with the high volume of available information, and interdiscplinary-ness of the position I am looking for (which is data scientist) can become a full-time job just searching for jobs. I use many different sources of job board, LinkedIn, Glassdoor, and Indeed to name a few and actively search for news related to the companies that I am interested in. I have accumulated more knowledge about companies that hire data scientist during last year than rest of my life. I believe that the point of time when someone is most interested in a company is when they are looking for career opportunities and while they are working. Therefore their opinions would be a good indicator for company's growth. 

## Project data
### Opinions data
 - **Linkedin Profiles**
 
This database tracks and records the number of employees across companies on daily basis and provides real time insight into how aggressively a company is growing vs its own plans and within its industry.

 - **Glassdoor reviews**
 
The data will consist of reviews on the company fromthe employees and employers.
 
### Performance data

- **Job Postings**

This database tracks individual job postings on corporate websites, allowing researchers and data scientists to view overall hiring plans of a company overtime. As well as historical data, users explore in a great detail what types of positions a company is looking to fill, where a company is looking to grow geographically, and in what specific product/business lines the company is looking to expand the most.

- **Stock prices**

This data will consist of stock prices over time for each company

## Preliminary Analysis
### LinkedIn follower trends
As a preliminary analysis I looked at the size of the followers for each company on LinkedIn and normalized for its size. As the estimation of company size, I used the number of employees on LinkedIn. 
The follower size can be divided into 3 groups, 0-100, 100-300 and 300-600. 
Which means the group that has larger follower size is attracting more followers online, which can be an indicator for potential growth

![fig1](https://github.com/hyojunada/data_incubator/blob/master/result/followers_to_size_ratio.png)


Then I looked at the changes in follower size (normalized over company's size) over time for individual companies in each industry
Shown below is the example for Investment Banking industry. From this I can identify which company's gaining more followers and whether it's growing faster or slower than the company norm. In [this notebook](https://github.com/hyojunada/data_incubator/blob/master/notebook/Section3-fig2_increase_of_followers_over_time.ipynb) you can do this for individual companies and see aggregated result for the entire industry. The aggregated result for the entire industry shows how much online interst the industry has compared to its size and whether the interest is growing or not. 

![fig2](https://github.com/hyojunada/data_incubator/blob/master/result/followers_size_over_time_Investment%20Banking.png)
