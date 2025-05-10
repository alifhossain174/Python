# s = "racecar"
# t = "carrace"
s = "jar"
t = "jar"

firstSet = set(s.lower())
secondSet = set(t.lower())

firstDict = dict()
secondDict = dict()

for characs in firstSet :
    firstDict[characs] = s.count(characs)

for characs in secondSet :
    secondDict[characs] = t.count(characs)

print(len(firstDict))

status = 0
for firstDictKey, firstDictValue  in firstDict.items() : 
    if firstDictKey in secondDict and secondDict[firstDictKey] == firstDictValue :
        status = 1
    else :
        status = 0

print(status)