#!/usr/bin/python3

# Installations
# pip install selenium
#Chrome driver for ubuntu https://tecadmin.net/setup-selenium-chromedriver-on-ubuntu/
# brew cask install chromedriver
# Need to allow the chromeDriver to run once from system preferance/security if it fails

# scheduling with cron
# crontab -e in the editor set the cron job as
# 0 10,19 * * * export PATH=/usr/local/bin/:$PATH && ~/Desktop/crons/hrms_login.py

# Full disk access
# You need to provide cron executable full disk access to execute the python code
# Make sure the python file is granted executable access i.e chmod u+x hrms_login.py

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium import webdriver
from bs4 import BeautifulSoup
import time
import datetime
import sys

profile=sys.argv[1]
location=sys.argv[2]
print(profile)
print(location)

options = Options()
options.add_argument("--start-maximized")

driver = webdriver.Chrome(chrome_options=options)
# driver.minimize_window()
print("Chrome started")

driver.get ("https://www.linkedin.com/jobs")
driver.find_element(by=By.XPATH, value="//input[@placeholder='Search job titles or companies']").send_keys(profile)
loc_elem = driver.find_element(by=By.XPATH, value="//input[@aria-controls='job-search-bar-location-typeahead-list']")
loc_elem.clear()
loc_elem.send_keys(location)
loc_elem.send_keys(webdriver.Keys.TAB)
driver.find_element(by=By.XPATH, value="//button[@data-tracking-control-name='homepage-jobseeker_search-jobs-search-btn']").click()
# driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

soup = BeautifulSoup(driver.page_source, 'html') 

# WAY2
jobs_html = soup.find_all('div', {'class':'base-search-card__info'})
final_jobs=[]
for job in jobs_html:
	final_jobs.append(job.select('h4')[0].text.strip()+'\t'+job.select('span',{'class':'job-search-card__location'})[0].text.strip()+'\t'+job.select('time',{'class':'job-search-card__listdate'})[0].get('datetime'))

for job in final_jobs:
	print(job)

print("Done...")


# WAY1
# Getting job titles
# jobs_html = soup.find_all('h3', {'class':'base-search-card__title'})
# job_titles = []
# for title in jobs_html:
# 	job_titles.append(title.text.strip())
  
# print(job_titles)

# # Getting job company name
# company_name_html = soup.find_all('a', {'data-tracking-control-name': 'public_jobs_jserp-result_job-search-card-subtitle'})
# company_names = []
  
# for name in company_name_html:
#     company_names.append(name.text.strip())
  
# print(company_names)

# # Job posting time
# jobs_date_html = soup.find_all('time', {'class': 'job-search-card__listdate'})
# dates = []
  
# for date in jobs_date_html:
#     dates.append(date.text.strip())
  
# print(dates)