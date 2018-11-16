from bs4 import BeautifulSoup
from send_email import SendEmail
import requests

def send_email(complete_str):
    mail = SendEmail()
    mail.message = complete_str
    mail.send()

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
    complete_str = new_listings + '\n----------------------------\n' + leaving
    send_email(complete_str)

if __name__ == '__main__':
    main()
