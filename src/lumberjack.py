from spec import *
import inspect
import sys
import re

function_arg_pattern = re.compile('\(.*\)')
unique_counter = 0

def main():
    if len(sys.argv) is not 3:
        print "Usage: python lumberjack.py <fileName> <injectQueryCode>"
    else:
        file_lines = 'from logger import *\n' + read_file(sys.argv[1]) + '\n'
        for log in log_functions:
            file_lines = log_function(file_lines, log[0], log[1])
        for log in log_function_args:
            file_lines = log_function_arg(file_lines, log[0], log[1])
        if sys.argv[2] == 'true':
           for query_str in inspect.getsourcelines(query)[0]:
               file_lines += query_str
           file_lines = 'import atexit\n' + file_lines + 'atexit.register(query)\n'

        print file_lines

def read_file(file_name):
    with open(file_name) as f:
        return f.read()

def log_function(file_lines, function_name, log_name):
    for method_match in extract_functions(file_lines, function_name):
        if not is_function_declaration(file_lines, method_match.end()):
            pos = method_match.start()
            c = file_lines[pos]
            while c is not ' ' and c is not '\t' and c is not '\n':
                pos -= 1
                c = file_lines[pos]
            pos += 1
            file_lines = file_lines[:pos] + 'log(\'' + log_name + '\', ' + \
                         file_lines[pos:method_match.end()] + ')' + \
                         file_lines[method_match.end():]
    return file_lines

def log_function_arg(file_lines, function_name, log_name):
    for function_match in extract_functions(file_lines, function_name):
        if not is_function_declaration(file_lines, function_match.end()):
            args = extract_args(function_match.group())
            if len(args) > 0 and args[0] is not '':
                function_string = function_match.group()
                for arg in reversed(args):
                    arg_pattern = re.compile(re.escape(arg))
                    arg_match = arg_pattern.search(function_string)
                    arg_pos = function_match.start() + arg_match.end()
                    file_lines = file_lines[:arg_match.start() + function_match.start()] + \
                                 'log(\'' + log_name + '\', ' + arg + ')' + file_lines[arg_pos:]
    return file_lines

def extract_functions(file_lines, function_name):
    function_pattern = re.compile(function_name + '\([a-zA-Z._$ 0-9]*\)')
    function_matches = re.finditer(function_pattern, file_lines)
    return reversed([method_match for method_match in function_matches])

def extract_args(function_string):
    args_match = re.search(function_arg_pattern, function_string)
    args_str = args_match.group()[1:len(args_match.group()) - 1]
    args = re.split(',', args_str)
    return [arg.strip() for arg in args]

def is_function_declaration(file_lines, function_end_pos):
    c = file_lines[function_end_pos]
    while c is ' ' or c is '\t' or c is '\n':
        function_end_pos += 1
        c = file_lines[function_end_pos]
    return c is ':'

if __name__ == "__main__": main()
