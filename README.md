# civicDataLabAssignment

##About the data source
The objective of a state treasury in India is to efficiently manage the financial resources of the state government. It collects funds, maintains financial records, prepares budgets, allocates resources, makes payments, and ensures transparency and accountability in financial matters. By performing these functions, the state treasury supports the overall governance and functioning of the state.
The state of Himachal Pradesh uses an Integrated Financial Management system to manage and disseminate various reports related to the state treasury department. The web platform contains several important reports which one can use to analyze the expenditures of the state government. 
At CivicDataLab, we have also integrated this data source into Himachal Pradesh Fiscal Data Explorer which can be further used to explore these reports visually. 

##Objective
As part of this assignment, we would like you to create a data pipeline to monitor a few reports, within this web platform, on a periodic basis. You will have to mine data from one of the reports, clean and process it, store the processed file in a database and then integrate all these steps in a data pipeline. Details about these steps is as follows: 
Steps
Start by mining data from  Himachal Pradesh Treasury portal Select 5 years from the date selection options
From Date :- 01/04/2018
To Date :- 31/03/2022
Select Report Data as per : Demand and HOA Wise Summary
Unit: Rupees
Perform following steps to clean the raw dataset:
Step 1: Drop all the rows where the columns HOA and DmdCd contains Total
Step 2: Fill all the blank cells in column DmdCd with relevant values 
Step 3: Split the column DmdCd at “-” and create two additional columns DemandCode and Demand from the splitted values.
Step 4: Split column HOA at “-” and expand the result to additional columns. These should be named as:
MajorHead
SubMajorHead
MinorHead
SubMinorHead
DetailHead
SubDetailHead
BudgetHead
PlanNonPlan
VotedCharged
StatementofExpenditure
Write a Python script to store the processed data in a SQLite database
During the call, we would like to discuss if there are other ways in which this database can further be normalised. 
Integrate above steps using a data pipeline. Use either Airflow or Prefect to automate the data flow.

##Output
A github repository with all relevant scripts and a well documented README file. Refer to the folder structure below:
Scripts
Docs
SQLite file
README

##Evaluation Parameters
Documentation of the process
Quality of code
Proactive communication - Let us know what you’re thinking, where you’re stuck, etc.

##Timeline
Do get back to us within 3-5 days. Feel free to reach out with any questions or clarifications during the process. If you're unable to dedicate as much time as you'd like but still have valuable thoughts and suggestions to share, please inform us.
How will we use your submission?
We will not use any of your output[s] for any commercial purposes. Your work remains yours and you are free to use it the way you want to. In case CivicDataLab ends up using any of your work in our live solution(s), we would ensure full disclosure and fair compensation to the creator accordingly.
Co-creation & Collaboration
At CivicDataLab, we believe in collaboration and co-creation. Feel free to discuss your work with us throughout the given time period either through email or through a scheduled call. We’re more than happy to provide continuous feedback, not just at the end of the task. In case you have any questions, don’t hesitate to ping us.


