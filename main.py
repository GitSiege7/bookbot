from stats import getWords, getFreq, sortDict

def getBookText(path):    
    with open(path) as f:
        contents = f.read()
    return contents

def printDict(chars):
    for char in chars:
        if char["char"].isalpha():
            print(char["char"], ": ", char["freq"])

def main():
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")

    numWords = len(getWords(getBookText("books/frankenstein.txt")))
    print("Found", numWords, "total words")

    print("--------- Character Count -------")

    freqDict = sortDict(getFreq(getBookText("books/frankenstein.txt")))
    printDict(freqDict)

main()