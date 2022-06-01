#!/usr/bin/python3

# Installations
# pip install selenium
# brew cask install chromedriver
# Need to allow the chromeDriver to run once from system preferance/security if it fails

# scheduling with cron
# crontab -e in the editor set the cron job as
# 0 10,19 * * * export PATH=/usr/local/bin/:$PATH && ~/Desktop/crons/hrms_login.py

# Full disk access
# You need to provide cron executable full disk access to execute the python code
# Make sure the python file is granted executable access i.e chmod u+x hrms_login.py

from selenium import webdriver
import time
import datetime

driver = webdriver.Chrome()
driver.minimize_window()
print("Chrome started")

driver.get ("https://hrms.opportune.in/TRUEFIT-ss/")
driver.find_element_by_id("UserName").send_keys("TF18080154")
driver.find_element_by_id("Password").send_keys("O3T3J6")
print("Logged in to HRMS")

driver.find_element_by_id("btnLogin").click()
html_source = driver.page_source

now = datetime.datetime.now()
today11am = now.replace(hour=11, minute=0, second=0, microsecond=0)

if(now < today11am):
	alreadyPunched = True
	print("Trying morning punch")
	while("Last Punch" not in html_source):
		alreadyPunched = False
		driver.find_element_by_id("btnPunch").click()
		driver.refresh()
		time.sleep(2)
	if(alreadyPunched):
		print("Already punched")
	else:
		print("Punched")

else:
	print("Trying Evening Punch")
	driver.find_element_by_id("btnPunch").click()
	time.sleep(2)
	driver.refresh()
	print("Punched")


print("Closing Chrome")
driver.quit()

