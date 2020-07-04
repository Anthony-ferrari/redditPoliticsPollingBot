import requests
from bs4 import BeautifulSoup

# get the data
data = requests.get('https://projects.fivethirtyeight.com/polls/')

# load data into bs4
soup = BeautifulSoup(data.text, 'html.parser')

# get data by looking for table 
div = soup.find('div', { 'class': 'day-container'})
dateAdded = div.find('h2', {'class': 'day'})
pollsTbody =div.find('tbody')

for tr in pollsTbody.findall('tr', {'class': 'new visible-row'}):
    pollName = tr.findall('td',{ 'class', 'type hide-mobile'}).find_all('a')[0].text.strip()
    

# classes that matter:

#### poll name block
# type hide-mobile first

#### dates block
# dates hide-mobile

#### pollster block
# pollster

#### sample block
# sample hide-mobile
# sample-type hide-mobile

#### results block
# answer hide-mobile
# value hide-mobile
# value hide-mobile (2nd value)
# answer hide-mobile (2nd value)

#### net result block
# leader hide-mobile
# net hide-mobile disapprove 

print(table)

    