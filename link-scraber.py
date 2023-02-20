from sys import argv
import validators
import requests


def request(validated_url):
    site = requests.get(validated_url).text
      

def validate_url(not_validated_url):
    valid_url=validators.url(not_validated_url)
    if valid_url:
        valid_url=not_validated_url
        print('URL is valid!')
        request(valid_url)
        
    else:
        print('Please Enter a Valid URL!')

def input_url():
    try:
        if len(argv) > 2:
            print('[~] Please Enter in valid format:\n\t |~| python link-scraber.py <url>')
        else:
            validate_url(argv[1])
    except:
        print('[~] Input argument could\' be empty!\n\t |~| python link-scraber.py <url>')
        
input_url()