from sys import argv
import validators
args = argv[1]

def validate_url(url):
    valid_url=validators.url(url)
    if valid_url:
        print('URL is ok!')
    else:
        print('Please Enter a Valid URL!')

def input_url(url):
    if len(args) > 1:
        print('[~] Please Enter in valid format:\n\t<~> python link-scraber.py <url>')
    else:
        validate_url(url)
        
input_url(args)