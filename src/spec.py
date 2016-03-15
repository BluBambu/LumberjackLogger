from logger import *

log_functions = [('test', 'test_log')]

log_function_args = [('test', 'test_args_log')]

def query():
    get_log('test_log').print_log()
    get_log('test_args_log').print_log()