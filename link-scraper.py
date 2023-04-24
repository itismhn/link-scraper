import argparse
import validators
import requests
from bs4 import BeautifulSoup

def request(validated_url):
    print("link scraping is started\n")
    try:
        site = requests.get(validated_url).text
        soup= BeautifulSoup(site, 'html.parser')
        links=soup.find_all("a")
        for link in links:
            href=link.get("href")
            if validators.url(href):
                print("link:",href)
    except:
        pass

def validate_url(not_validated_url):
    valid_url=validators.url(not_validated_url)
    if valid_url:
        valid_url=not_validated_url
        print('URL is valid!\n')
        request(valid_url)
        
    else:
        print('Please enter a valid URL!')

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='My custom description for this script.', 
                                     usage='%(prog)s  url')

    parser.add_argument('url', metavar='URL', type=str,
                        help='the URL of the website to scrape')

    args = parser.parse_args()


    validated_url = validate_url(args.url)
