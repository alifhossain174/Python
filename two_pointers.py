# check has pair with sum
# array is [1, 4, 7, 10] and target 11

def hasPairWithSum(myList, target):
    myList.sort()
    leftSide = 0
    rightSide = len(myList) - 1

    while leftSide < rightSide:
        total = myList[leftSide] + myList[rightSide]
        if total == target:
            return True
        elif total < target:
            leftSide += 1
        else:
            rightSide -= 1

    return False


print(hasPairWithSum([10, 5, 7, 3], 11))