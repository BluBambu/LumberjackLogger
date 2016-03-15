def main():
    print len(foo('boo', 'baz'))
    print bar(234.2, 44).is_integer()

def foo(a, b):
    return a

def bar(c, d):
    return foo(c, 0)

if __name__ == "__main__": main()