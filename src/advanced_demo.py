def main():
    with open('./urls.txt') as f:
        for url in f:
            process(url)

def process(url):
    print url

if __name__ == "__main__": main()