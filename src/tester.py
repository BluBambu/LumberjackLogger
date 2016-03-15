import atexit
from logger import *
def main():
    print log('function_log', len(foo(log_arg('args_log', 'boo', 2), log_arg('args_log', 'baz', 2))))
    print bar(log_arg('args_log', 234.2, 0), log_arg('args_log', 44, 0)).is_integer()

def foo(a, b):
    return a

def bar(c, d):
    return log('function_log', foo(log_arg('args_log', c, 1), log_arg('args_log', 0, 1)))

if __name__ == "__main__": main()
def query():
    print 'logs:'
    get_log('function_log').print_log()
    get_log('args_log').print_log()
atexit.register(query)

