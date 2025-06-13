dataList = [1, 3, 5, 7, 9]
target = 4


def binarySearch(dataList, target):

    leftSide = 0
    rightSide = len(dataList)-1

    while leftSide <= rightSide:
        mid = (leftSide + rightSide) // 2
        if dataList[mid] == target:
            return True
        elif dataList[mid] < target:
            leftSide = mid + 1
        else:
            rightSide = mid - 1

    return False

print(binarySearch(dataList, target))
    