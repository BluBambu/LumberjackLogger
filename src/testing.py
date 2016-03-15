import atexit
from logger import *
def main():
    print log('test_log', test(log('test_args_log', 234.0).is_integer()))

def test(f):
    return f

if __name__ == "__main__": main()
def query():
    get_log('test_log').print_log()
    get_log('test_args_log').print_log()
atexit.register(query)

