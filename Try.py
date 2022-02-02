from bs4 import BeautifulSoup
import bs4 as bs
import requests
query = input("Enter country name or world: ")
url = 'https://www.worldometers.info/coronavirus/'
page = requests.get(url)
soup = BeautifulSoup(page.content, 'lxml')
totalcases = soup.findAll('div', attrs =  {'class': 'maincounter-number'})
total_cases = []
for total in totalcases:
    total_cases.append(total.find('span').text)
world_total = 'Total Coronavirus Cases: ' + total_cases[0]
world_deaths = 'Total Deaths: ' + total_cases[1]
world_recovered = 'Total Recovered: ' + total_cases[2]

info = 'For more information visit: ' + 'https://www.worldometers.info/coronavirus/#countries'
if 'world' in query:
    print('World Updates: ')
    print(world_total)
    print(world_deaths)
    print(world_recovered)
    print(info)
else:
    country = query
    url = 'https://www.worldometers.info/coronavirus/country/' + country.lower() + '/'
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'lxml')
    totalcases = soup.findAll('div', attrs =  {'class': 'maincounter-number'})
    total_cases = []
    for total in totalcases:
        total_cases.append(total.find('span').text)
    total = 'Total Coronavirus Cases: ' + total_cases[0]
    deaths = 'Total Deaths: ' + total_cases[1]
    recovered = 'Total Recovered: ' + total_cases[2]
    info = 'For more information visit: ' + url
    updates = country.capitalize() + ' Updates: '
    print(updates)
    print(total)
    print(deaths)
    print(recovered)
    print(info)