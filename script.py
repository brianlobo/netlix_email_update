from bs4 import BeautifulSoup
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import requests
import smtplib


def send_email(complete_str):
    email = 'brianlobo.bot@gmail.com'
    password = 'PASSWORD'
    send_to_email = 'brianlobo.code@gmail.com'
    subject = 'New Netflix Listings!'
    message = complete_str

    msg = MIMEMultipart()
    msg['From'] = email
    msg['To'] = send_to_email
    msg['Subject'] = subject

    msg.attach(MIMEText(message, 'plain'))
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(email, password)
    text = msg.as_string()
    server.sendmail(email, send_to_email, text)
    server.quit()
    print("---Success---")

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
    complete_str = new_listings + '\n-------------\n' + leaving
    send_email(complete_str)

if __name__ == '__main__':
    main()
