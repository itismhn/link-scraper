from sys import argv
import validators

def validate_url(url):
    valid_url=validators.url(url)
    if valid_url:
        print('URL is ok!')
    else:
        print('Please Enter a Valid URL!')

def input_url():
    try:
        #args = argv
        if len(argv) > 2:
            print('[~] Please Enter in valid format:\n\t<~> python link-scraber.py <url>')
        else:
            validate_url(argv)
    except:
        pass
        
input_url()