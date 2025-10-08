inputArray = [1,1,2,2,3,3]
inputArray.sort()
target = 1

uniqePossiblePairs = set()
for i in range(len(inputArray)):
    for j in range(i+1, len(inputArray)):
        if abs(inputArray[i] - inputArray[j]) == target:
            uniqePossiblePairs.add(tuple(sorted((inputArray[i], inputArray[j]))))
            

print(len(uniqePossiblePairs))