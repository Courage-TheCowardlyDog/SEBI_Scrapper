# For internship @ FindMind Analytics
Python Scripts:  
* Scheduler.py - Program to schedule the job to be run @ 9pm daily -> Stores the CronJob to Scheduler.tab  
* SEBI_Scrapper - Program to scrap the given URL for PDFs as instructed -> Stores the Links to PDF_Database.xlsx  
  
Supporting Files:  
* Scheduler.tab - The Python-CronTab jobs get written to this file.
* PDF_Database.xlsx - Contains the scrapped links to the PDFs.  
  
Libraries Used:
* python-crontab - For scheduling the job.  
* openpyxl - To write the data to an excel file.  
* ssl - To ignore certification errors.  
* bs4 - To parse the HTML code from the website.  
* urllib (requests) - To access the websites.  
