import sys
import validators
import requests
from bs4 import BeautifulSoup

def request(validated_url):
    try:
        site = requests.get(validated_url).text
        soup= BeautifulSoup(site, 'html.parser')
        links=soup.find_all("a")
        for link in links:
            href=link.get("href")
            if validators.url(href):
                print("link:",href)
    except:
        print('Error...')
        pass

def validate_url(not_validated_url):
    valid_url=validators.url(not_validated_url)
    if valid_url:
        valid_url=not_validated_url
        print('URL is valid!\nlink scrabing is started\n')
        request(valid_url)
        
    else:
        print('Please Enter a Valid URL!')

def input_url():
    try:
        if len(sys.argv) > 2:
            print('[~] Please Enter in valid format:\n\t |~| python link-scraber.py <url>')
        else:
            validate_url(sys.argv[1])
    except:
        print('[~] Input argument could\'t be empty!\n\t |~| python link-scraber.py <url>')
        sys.exit()
        
input_url()