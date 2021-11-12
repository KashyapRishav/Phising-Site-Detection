# machine_learning_projects
# end_to_end-machine-learning-phising detetction system
## PHISING-   
Phishing is a cybercrime in which a target or targets are contacted by email,
telephone or text message by someone posing as a legitimate institution to lurendividuals into providing sensitive data 
such as personally identifiable information, banking and credit card details, and passwords

## prevent phising attacks:
To protect against spam mails, spam filters can be used.
Generally, the filters assess the origin of the message, the software used to send the message
, and the appearance of the message to determine if it’s spam.
Occasionally, spam filters may even block emails from legitimate sources, so it isn’t always 100% accurate.


## DATA COLLECTION : Data taken from Kaggle open source platform.
About dataset :
 Data is containg 5,49,346 unique entries.
There are two columns.
Label column is prediction col which has 2 categories A. Good - which means the urls is not containing malicious stuff and this site is not a Phishing Site. B. Bad - which means the urls contains malicious stuffs and this site isa Phishing Site.


### This is a supervised machine learning task. There are two major types of supervised  machine learning problems, 
Classification and regressions.
This data set comes under classification problem, as the input Urls is classified as bad(phising) or good(legitimate).
The machine learning models (classification) considered to train the dataset in this notebook are:
1. logistic regression
2. multinomialNB

## Deployment

This model is deployed using Django framework.
