import selenium
from selenium import webdriver as wb
from selenium.webdriver.common.by import By
import time
import csv
import requests
import json
import random
from bs4 import BeautifulSoup

   #    Scraping Restaurant Links

resultsfile = open("res.csv", 'a', encoding='utf8', newline='')
resultswriter = csv.writer(resultsfile)
resultswriter.writerow(['Id', 'Link'])

driver = wb.Chrome()
driver.get("https://www.swiggy.com/city/bangalore/best-restaurants")
i=0
while True:
    time.sleep(2)
    try:
        driver.find_element(By.CSS_SELECTOR,'div.sc-beySbM.evFhcR').click()
    except:
        print("error")
    divs = driver.find_elements(By.CSS_SELECTOR,'div.sc-gLLvby.jXGZuP > div')
    for div in divs:
        resultswriter.writerow([i, div.find_element(By.CSS_SELECTOR,'a').get_attribute('href')])
    i+=1
    print(i)
    if(len(divs) >= 500):
        break
