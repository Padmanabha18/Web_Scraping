import requests
from bs4 import BeautifulSoup
import pandas as pd


def extract(page):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36'}
    url = f'https://in.indeed.com/jobs?q=python+developer&l=Bangalore%2C+Karnataka&start={page}'
    r = requests.get(url, headers)
    soup = BeautifulSoup(r.content, 'html.parser')
    return soup


def change(soup):
    loc = soup.find_all('div', class_='jobsearch-SerpJobCard')
    for item in loc:
        title = item.find('a').text.strip()
        company = item.find('span', class_='company').text.strip()
        try:
            salary = item.find('span', class_='salaryText').text.strip()
        except:
            salary = ''
        summary = item.find('div', class_='summary').text.strip()
        job = {'title': title, 'company': company, 'salary': salary, 'summary': summary}
        joblist.append(job)
    return


joblist = []
for i in range(0, 40, 10):
   c = extract(1)
change(c)

df = pd.DataFrame(joblist)
print(df.head())
df.to_csv('jobs.csv')
