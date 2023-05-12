import requests
from bs4 import BeautifulSoup
import re 
# Replace this with the URL you want to scrape
def scrap(text) :
    try :
        url_pattern = re.compile(r'https?://\S+')
        url_text = url_pattern.findall(text)[0]


        response = requests.get(url_text)
        data = response.text
        soup = BeautifulSoup(data, 'html.parser')
        text = text.replace(url_text,soup.body.get_text())
        return text
    except :
        return text

        