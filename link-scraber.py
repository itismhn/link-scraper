from sys import argv
import validators

def validate_url(url):
    valid_url=validators.url(url)
    if valid_url:
        print('URL is valid!')
        
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