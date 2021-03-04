import requests
from bs4 import BeautifulSoup
import pandas as pd


jobTitles = []
companyName = []
locations = []
links = []
discription = []
postDate = []


page = requests.get("https://www.linkedin.com/jobs/search/?geoId=102713980&keywords=software%20data%20engineer&location=India")
soup = BeautifulSoup(page.content, 'html.parser')
jobs = soup.find_all('div', class_="result-card__contents job-result-card__contents")



# to get the titles of the jobs
titles = soup.find_all('h3', class_="result-card__title job-result-card__title")
for title in titles:
    jobTitles.append(title.get_text())
    
    

# to get the name of the company
names = soup.find_all('a', class_="result-card__subtitle-link job-result-card__subtitle-link")
for name in names:
    try:
        companyName.append(name.get_text())
    except:
        companyName.append("not available")



# to get the links to apply for the job
for job in jobs:
    try:
        links.append(job.find('a')['href'])
    except:
        links.append("not available")



# to get the location of the job
places = soup.find_all('span', class_="job-result-card__location")
for place in places:
    locations.append(place.get_text())



# a short discription about the job
phrases = soup.find_all('p', class_="job-result-card__snippet")
for phrase in phrases:
    discription.append(phrase.get_text())



# date when the job was posted
for job in jobs:
    try:
        postDate.append(job.find('time')['datetime'])
    except:
        postDate.append("not available")



d = {
    "Job title": jobTitles,
    "Company Name": companyName,
    "Location": locations,
    "Apply Here": links,
    "Skills": discription,
    "Posted on": postDate
}


data = pd.DataFrame(d)
data.to_csv('jobs.csv')
