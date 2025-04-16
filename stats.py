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

def sortDict(unsortedDict):
    chars = []

    for key in unsortedDict:
        chars.append({"char" : key, "freq" : unsortedDict[key]})

    chars.sort(reverse=True, key=sortBy)

    return chars

def sortBy(dict):
    return dict["freq"]