myList = [1, 2, 3, 4, 5]

# find max sum of any 3 consecutive numnbers

maxSum = 0
for i in range(len(myList)-2):
    currentSum = myList[i] + myList[i+1] + myList[i+2]
    if currentSum > maxSum:
        maxSum = currentSum
        
print(maxSum)

