def getWords(text):
    words = text.split()
    return words

def getFreq(text):
    charFreq = {}
    for char in text.lower():
        if char in charFreq:
            charFreq[char] += 1
        else:
            charFreq[char] = 1
    return charFreq