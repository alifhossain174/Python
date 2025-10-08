sentence = 'Time to write good code'


def longestEvenWord(sentence):
    myList = sentence.split()
    longestlengthIndex = []
    currentLargestLength = 0

    for i in range(len(myList)):
        if len(myList[i])%2 == 0 and len(myList[i]) > currentLargestLength:
            longestlengthIndex.append(i)
            currentLargestLength = len(myList[i])

    if len(longestlengthIndex) > 0:
        return myList[min(longestlengthIndex)]
    else:
        return '00'


print(longestEvenWord(sentence))