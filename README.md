# Allocate Resources Python Algorithm
Hi guys! I wrote this algorithm on Python (with the help of ChatGPT) to assist in the allocation of GP clinics during GP week in a fair manner.
I've decided to publish it for future batches to benefit from this as well.

This algorithm allows for allocation based on choice followed by first-come-first-serve basis.
This means that all 1st choices will be allocated first, followed by 2nd choices and so on.
In the event that the number of 1st choices exceed the number of slots of a clinic, it will be allocated in a first-come-first serve basis.
This algorithm also assumes that there are 2 slots available for every clinic. 


**How to read the code**

Choices = Names of clinics that can be chosen
Submissions = Preferences submitted by students
Person = Student
Rank = Ranked choices (1st choice, 2nd choice, 3rd choice, ...)


**How to run this code!**

You will need to install Python to run this code.
It also includes some functions that require additional installations, namely:
1. pandas
2. openpyxl
You can install these after installing Python by entering the following in command prompt(WIN)/terminal(MAC)
  pip3 install pandas
  pip3 install openpyxl
 
 
You will need to prepare 2 excel sheets; templates have been provided in the zip file "Templates":
1. Choices - Names of all the clinics available
2. Submissions - Preferences submitted by students
**Choices**
- Heading of the table must be named "Choice" for the code to recognise the list
**Submissions**
- Headings must be "Person" for students, "Rank" for ranked choices
- Ranked choices must be formatted in this manner: 1st choice,2nd choice,3rd choice,etc...
- Use "concatenate" function in excel to convert your google form response into the needed format for ranked choices :)


Copy path link of the excel sheets into the code:
- Clinic Names (Choices): substitute 'path/to/your/choices/file.xlsx'
- Student Preferences (Submissions): substitute 'path/to/your/submissions/file.xlsx'

This code exports the final allocations into an excel file, you will need to specify where to export it to:
- Substitute 'path/to/your/output/file.xlsx' with your desired path, and add the file name you prefer at the back
- E.g. '/Users/crystalgoh/Desktop/Final Allocations.xlsx'
