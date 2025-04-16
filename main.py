import sys
from stats import getWords, getFreq, sortDict

def getBookText(path):    
    with open(path) as f:
        contents = f.read()
    return contents

def printDict(chars):
    for char in chars:
        if char["char"].isalpha():
            print(f"{char["char"]}: {char["freq"]}")

def main():
    if(len(sys.argv) != 2):
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")

    numWords = len(getWords(getBookText(sys.argv[1])))
    print("Found", numWords, "total words")

    print("--------- Character Count -------")

    freqDict = sortDict(getFreq(getBookText(sys.argv[1])))
    printDict(freqDict)

    print("============= END ===============")

main()