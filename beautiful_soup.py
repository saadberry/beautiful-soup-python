from bs4 import BeautifulSoup
import requests
from pathlib import Path
import csv

p = Path(__file__).with_name('index.html')
with p.open('r') as f:
    # print(f.read())
    soup = BeautifulSoup(f,'lxml')

csv_file=open('scraped_data.csv','w') 

csv_writer = csv.writer(csv_file)
csv_writer.writerow(['headline','summary'])


# print(soup.prettify())
for article in soup.find_all('div', class_='article'):

    #getting headline of article 2
    headline = article.h2.a.text
    print(headline)

    #getting summary of article
    summary = article.p.text
    print(summary)

    #printing blank line as a seperator b/w the articles
    print()

    csv_writer.writerow([headline,summary])

csv_file.close()

