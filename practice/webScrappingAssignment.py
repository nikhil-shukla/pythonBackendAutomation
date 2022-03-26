import requests
from bs4 import BeautifulSoup as bs

baseUrl = "https://rahulshettyacademy.com/"
data = requests.get(baseUrl + "/AutomationPractice/")
soup = bs(data.content, 'html.parser')
# print(soup.prettify())

courseTable = soup.find('table',{'id':'product'})
# print(courseTable.prettify())

data = courseTable.findAll('tr')
print(data)
for d in data:
    if d.find('td'):
        col = d.find('td')
        print(col.text)

