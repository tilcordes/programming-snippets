from bs4 import BeautifulSoup
import requests

def get_ticketlinks():
    r = requests.get(url='https://shop.hsv.de/deutsch/tickets/heimspiele/')
    soup = BeautifulSoup(r.text, 'html5lib')

    for link in soup.find_all('a', class_='hsv-ticket__title'):
        print(link['href'])

def get_headline():
    r = requests.get(url='https://hsv.de/')
    soup = BeautifulSoup(r.text, 'html5lib')

    headline = soup.find('p', class_='text-align-nav')
    print(headline.text)

def get_htmltext():
    r = requests.get(url='https://hsv.de')
    soup = BeautifulSoup(r.text, 'html5lib')

    htmltext = soup.prettify()
    print(htmltext)