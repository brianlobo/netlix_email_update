from bs4 import BeautifulSoup
import requests

def get_listings(url):
    source_code = requests.get(url).text
    soup = BeautifulSoup(source_code, 'lxml')
    article = soup.find("article", class_="m-content").text
    new_str = article.find('Everything new on Netflix')
    leaving_str = article.find('Leaving Netflix')
    new_listings = article[new_str : leaving_str]
    leaving = article[leaving_str:]
    return new_listings, leaving

def main():
    new_listings, leaving = get_listings('https://www.digitaltrends.com/home-theater/new-on-netflix/')

if __name__ == '__main__':
    main()
