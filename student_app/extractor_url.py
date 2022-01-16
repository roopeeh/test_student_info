import requests
from bs4 import BeautifulSoup


def extract_all_links(site):
    '''
    returns links 

    extracts all availble links for a give perameter string and returns as list.
    '''
    html = requests.get(site).text
    soup = BeautifulSoup(html, 'html.parser').find_all('a')
    links = [link.get('href') for link in soup]
    return links
