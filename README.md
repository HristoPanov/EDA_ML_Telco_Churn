### Intro

Customer churn is one of the most important metrics for a service business to evaluate. While it's not the happiest measure, it's a number that can give a company the hard truth about its customer retention.
It's hard to measure success if you don't measure the inevitable failures, too. While you strive for 100% of customers to stick with your company, that's simply unrealistic. That's where customer churn comes in.

Moreover, sometimes it costs more to acquire new customers than it does to retain existing ones.

But are there any data, characteristics or evidence accumulated through the business cycle that could help the companies further distinguish or identify potential churn? Could the already churned customers be used as a means of understanding why customers are leaving and what could be the main drivers for that. 

The current document and the performed analysis will be focused on the exploration of the main features of customers who Churn.
Moreover, it will be following the exploration of the main characteristics of this so important group of customers, how could they be defined and pointing out main indicators that would help the process of identification.

Main questions - are there any specific characteristics that could help the identification of Churn.

In addition - a quick and dirty (no preliminary feature selection, pair of variables with correlation removal, etc., no estimation coefficient sanity and adequacy check is performed) modelling approach is applied for prediction of Churn and TotalCharges aiming to set a starting point for further analysis.

The sample dataset contains information from a Telco company about their portfolio of customers and more specifically if some of them have left the services and abandoned the company within a specific month.


![Churn Image](https://d1jnx9ba8s6j9r.cloudfront.net/blog/wp-content/uploads/2018/07/Customer-Churn-528x295.png)

### Process Description
1. Data Import
2. Data Audit
3. Churn Volumes and Churn Rate
4. Features Correlation
5. Numerical Variables Exploration
6. Categorical Variables Exploration
7. Data Preprocessing for Modeling
8. Modelling
    * Logistic Regression
    * Linear Regression
    * Decision Tree


### Data Description

Each row represents a customer, each column contains customer’s attributes.
The data set includes information about:
- Customers who left – the column is called Churn
- Services that each customer has signed up for : phone, multiple lines, internet, online security, online backup, device protection, tech support, and streaming TV and movies
- Customer account information – how long they’ve been a customer, contract, payment method, paperless billing, monthly charges, and total charges
- Demographic info about customers – gender, and if they have partners and dependents

#### Columns

__customerID__: Customer ID  
__gender__: Whether the customer is a male or a female  
__SeniorCitizen__: Whether the customer is a senior citizen or not (1, 0)  
__Partner__: Whether the customer has a partner or not (Yes, No)  
__Dependents__: Whether the customer has dependents or not (Yes, No)  
__tenure__: Number of months the customer has stayed with the company  
__PhoneService__: Whether the customer has a phone service or not (Yes, No)  
__MultipleLines__: Whether the customer has multiple lines or not (Yes, No, No phone service)  
__InternetService__: Customer’s internet service provider (DSL, Fiber optic, No)  
__OnlineSecurity__: Whether the customer has online security or not (Yes, No, No internet service)  
__OnlineBackup__: Whether the customer has online backup or not (Yes, No, No internet service)  
__DeviceProtection__: Whether the customer has device protection or not (Yes, No, No internet service)  
__TechSupport__: Whether the customer has tech support or not (Yes, No, No internet service)  
__StreamingTV__: Whether the customer has streaming TV or not (Yes, No, No internet service)  
__StreamingMovies__: Whether the customer has streaming movies or not (Yes, No, No internet service)  
__Contract__: The contract term of the customer (Month-to-month, One year, Two year)  
__PaperlessBilling__: Whether the customer has paperless billing or not (Yes, No)  
__PaymentMethod__: The customer’s payment method (Electronic check, Mailed check, Bank transfer (automatic), Credit card (automatic))  
__MonthlyCharges__: The amount charged to the customer monthly  
__TotalCharges__: The total amount charged to the customer  
__Churn__: Whether the customer churned or not (Yes or No)    

### Result Summary

Based on the analysis of the provided data, if we are about the identify the potential profile of Customer ceases his relation with the Company (aka Churn) we would have to consider the following:
- They have higher MonthlyCharges on average.
- More recent customers are more likely to Churn.
- Customers without a Partner and Dependants are significantly more likely to Churn.
- Customers with 'Fiber Optic' as an InternetService are significantly more likely to Churn then others.
- Customers without (aka flagged with "No") by one of the variables - 'OnlineSecurity','DeviceProtection','TechSupport' are more likely to leave.
- Customers without (aka flagged with "No OnlineBackup') 'OnlineBackup' are more likely to abandon the service.
- Moreover, Customers with 'Month-to-Month' Contract are very likely to leave.
- A very significant identification for Churn is 'PaymentMethod' equal to 'Electronic check'. Moreover, from those with 'Electronic check' and also have 'PaperlessBilling' equal to 'Yes' are significantly likely to abandon the service.


### Reference

https://www.kaggle.com/blastchar/telco-customer-churn