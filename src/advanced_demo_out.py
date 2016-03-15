import atexit
from logger import *
def main():
    with open('./urls.txt') as f:
        for url in f:
            process(log_arg('url_log', url, 0))

def process(url):
    print url

if __name__ == "__main__": main()
def query():

    import re
    regex = re.compile(
            r'^(?:http|ftp)s?://' # http:// or https://
            r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|' #domain...
            r'localhost|' #localhost...
            r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})' # ...or ip
            r'(?::\d+)?' # optional port
            r'(?:/?|[/?]\S+)$', re.IGNORECASE)

    def handle_url(urls):
        for url in urls[0]:
            if regex.match(url) is not None:
                log('valid_url', url)
            else:
                log('invalid_url', url)

    get_log('url_log').map(handle_url)

    print 'Valid URLs:'
    get_log('valid_url').print_log()
    print 'Invalid URLs:'
    get_log('invalid_url').print_log()
atexit.register(query)

