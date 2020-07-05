import requests
from bs4 import BeautifulSoup
def fivethirtyeight():
    # get the data
    data = requests.get('https://projects.fivethirtyeight.com/polls/')

    # load data into bs4
    soup = BeautifulSoup(data.text, 'html.parser')

    # create list for items 
    pollList = []

    # get data by looking for table 
    div = soup.find('div', { 'class': 'day-container'})
    dateAdded = div.find('h2', {'class': 'day'})
    pollsTbody =div.find('tbody')

    newString = ""

    for tr in pollsTbody.find_all('tr', {'class': 'visible-row'}):
        pollName = tr.find_all('td',{ 'class', 'type'})[0].text.strip()

        datePosted = tr.find_all('td', {'class','dates hide-mobile'})[0].find_all('div')[0].text.strip()

        pollster = tr.find_all('td', {'class', 'pollster'})[0].find_all('a')[1].text.strip()

        sampleSize = tr.find_all('td', {'class', 'sample'})[0].text.strip()

        sampleSizeType = tr.find_all('td', {'class', 'sample-type'})[0].text.strip()

        approvePercent = tr.find_all('td', {'class', 'value'})[0].find_all('div')[0].text.strip()

        disapprovePercent = tr.find_all('td', {'class', 'value'})[1].find_all('div')[0].text.strip()

        netResultName = tr.find_all('td', {'class', 'leader'})[0].text.strip()
        netResultValue = tr.find_all('td', {'class', 'net'})[0].text.strip()
        netResult = netResultName + " " + netResultValue


        newString += " | " + pollName + " | " + datePosted + " | " + pollster + " | " + sampleSize + " | " + sampleSizeType + " | " + approvePercent + " | " + disapprovePercent + " | " + netResult + " | \n"
        pollList.append(newString)
    return pollList

fivethirtyeight()

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

    