import atexit
from logger import *
def main():
    print log('add_log', add(1, 2))
    print mult(log_arg('mult_log', 5, 0), log_arg('mult_log', 1, 0))

def add(a, b):
    return a + b

def mult(c, d):
    sum = 0
    for i in range(c):
        sum = log('add_log', add(sum, d))
    return sum

if __name__ == "__main__": main()
def query():
    print 'add log:'
    get_log('add_log').print_log()
    print 'mult log:'
    get_log('mult_log').print_log()
atexit.register(query)

