import atexit
from logger import *
def main():
    for x in [1, 2, 0, -5, -190, 23, -33]:
        log('no_negatives_log', no_negative_ret(x))

def no_negative_ret(x):
    return x

if __name__ == "__main__": main()
def query():
    def sqrt_filter(x):
        return x[0] < 0
    get_log('no_negatives_log').filter(sqrt_filter).print_log()
atexit.register(query)

