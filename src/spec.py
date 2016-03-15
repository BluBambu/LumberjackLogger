from logger import *

log_functions = [('foo', 'function_log')]

log_function_args = [('bar', 'args_log'), ('foo', 'args_log')]

def query():
    print '\nlogs:'
    get_log('function_log').print_log()
    get_log('args_log').print_log()
