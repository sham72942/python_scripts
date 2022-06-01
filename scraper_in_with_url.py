#!/usr/bin/python3

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium import webdriver
from bs4 import BeautifulSoup
import time
import datetime
import sys
import csv
import urllib.parse
from pathlib import Path

profile=sys.argv[1]
print('Profile is:',profile)
location=sys.argv[2]
print('location is:',location)
base_uri='https://www.linkedin.com/jobs/search/?f_TPR=r86400&geoId=102713980'
home = str(Path.home())
csvPath = home+'/'+profile+' '+location+'.csv'
print('output file path is: ',csvPath)

def writeCsvHeaders(path):
	file=open(path, 'w', newline='')
	writer = csv.writer(file)
	header=['Title','Company Name','Date Posted','Location']
	writer.writerow(header)
	file.close()

def writePageDetails(path, browser, offset):
	file=open(csvPath, 'a', newline='')
	writer = csv.writer(file)
	soup = BeautifulSoup(chrome.page_source, features="html.parser")
	jobs_html = soup.find_all('div', {'class':'base-search-card__info'})[offset:]
	for job in jobs_html:
		title=job.select('h3')[0].text.strip()
		company=job.select('h4')[0].text.strip()
		# location=job.select('span',{'class':'job-search-card__location'})[0].text.strip()
		date_posted = job.select('time',{'class':'job-search-card__listdate'})[0].get('datetime')
		writer.writerow([title,company,date_posted,location])
	file.close()

uri=base_uri+'&'+'keywords='+urllib.parse.quote(profile)+'&'+'location='+urllib.parse.quote(location)

options = Options()
options.add_argument("--start-maximized")

chrome = webdriver.Chrome(options=options)
print("Chrome started")

writeCsvHeaders(csvPath)

chrome.get(uri)
offset=0
while(True):
	time.sleep(1)
	chrome.execute_script("window.scrollTo(0,document.body.scrollHeight)")
	writePageDetails(csvPath, chrome, offset)
	soup = BeautifulSoup(chrome.page_source, features="html.parser")
	job_count = len(soup.find_all('div', {'class':'base-search-card__info'}))
	if(job_count==offset):
		break
	else:
		offset=job_count


chrome.quit()