from stats import getWords, getFreq

def getBookText(path):    
    with open(path) as f:
        contents = f.read()
    return contents

def main():
    print(len(getWords(getBookText("books/frankenstein.txt"))), "words found in the document")
    print(getFreq(getBookText("books/frankenstein.txt")))

main()