from stats import getWords

def getBookText(path):    
    with open(path) as f:
        contents = f.read()
    return contents

def main():
    print(len(getWords(getBookText("books/frankenstein.txt"))), "words found in the document")

main()