def main():
    print add(1, 2)
    print mult(5, 1)

def add(a, b):
    return a + b

def mult(c, d):
    sum = 0
    for i in range(c):
        sum = add(sum, d)
    return sum

if __name__ == "__main__": main()