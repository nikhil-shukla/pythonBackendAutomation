import requests
from bs4 import BeautifulSoup as bs

baseUrl = "https://www.imdb.com"
data = requests.get(baseUrl + "/find?s=ep&q=thriller&ref_=nv_sr_sm")
soup = bs(data.content, 'html.parser')
# print(soup.prettify())

moviesTable = soup.find('table', {'class': 'findList'})
# print(moviesTable.prettify())
rows = moviesTable.findAll('tr')

for row in rows:
    rowData = row.findAll('td')
    movie = rowData[1].a.text
    # print(movie)
    subUrl = rowData[1].a['href']
    subData = requests.get(baseUrl + subUrl)
    childSoup = bs(subData.content, 'html.parser')

    if childSoup.find('li', {'class': 'ipc-inline-list__item'}):
        genre = childSoup.find('li', {'class': 'ipc-inline-list__item'})
        if genre.text == 'Thriller':
            # print(genre.text)
            print(movie)
