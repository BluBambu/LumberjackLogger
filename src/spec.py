from logger import *

# Easy Demo

"""

log_functions = [('no_negative_ret', 'no_negatives_log')]

log_function_args = []

def query():
    def sqrt_filter(x):
        return x[0] < 0
    get_log('no_negatives_log').filter(sqrt_filter).print_log()

"""

# Intermediate Demo

"""

log_functions = [('add', 'add_log')]

log_function_args = [('mult', 'mult_log')]

def query():
    print 'add log:'
    get_log('add_log').print_log()
    print 'mult log:'
    get_log('mult_log').print_log()

"""

# Advanced Demo

"""

log_functions = []

log_function_args = [('process', 'url_log')]

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

"""
