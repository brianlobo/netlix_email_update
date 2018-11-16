from bs4 import BeautifulSoup
import requests

source_code = requests.get('https://www.digitaltrends.com/home-theater/new-on-netflix/').text
soup = BeautifulSoup(source_code, 'lxml')
print(soup.prettify())
