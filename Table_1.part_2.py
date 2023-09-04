import selenium
from selenium import webdriver as wb
from selenium.webdriver.common.by import By
import time
import csv
import requests
import json
import random
from bs4 import BeautifulSoup


# Scraping Each Restaurant Data Table 1

resultsfile = open("table1.csv", 'a', encoding='utf8', newline='')
resultswriter = csv.writer(resultsfile)
resultswriter.writerow(['ID','Link','Name','Rating','Price','Cuisines'])

csvfile = open('res.csv','r', encoding='utf-8', newline='')
links = list(csv.reader(csvfile))


headers = {
    'authority': 'www.swiggy.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9,fr;q=0.8',
    'cache-control': 'max-age=0',
    'referer': 'https://www.swiggy.com/city/bangalore/best-restaurants',
    'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
}


check=0
random_requests_number = random.randint(5, 10)
i=0
for link in links[1:]:
    print(link[1],i)
    try:
        response = requests.get(f'{link[1].strip()}',headers=headers)
        if(random_requests_number-check==0):
            check=0
            random_delay_number = random.randint(2, 6)
            print(f"delaying after {random_requests_number} requests for {random_delay_number} seconds processing {i}")
            time.sleep(random_delay_number)
            random_requests_number = random.randint(3, 6)
        check+=1
        soup = BeautifulSoup(response.text, 'html.parser')
        time.sleep(1)
        jsondata = json.loads(soup.find('script',{'type': 'application/ld+json'}).text)
        name = jsondata['name']
        try:
            rating = jsondata['aggregateRating']['ratingValue']
        except:
            rating = ''
        try:
            price = jsondata['priceRange']
        except:
            price = ''
        try:
            cousine = jsondata['servesCuisine']
        except:
            cousine = ''

        resultswriter.writerow([link[0], link[1], name, rating,price, cousine])
    except:
        print("error")
        input('v')
    i+=1




