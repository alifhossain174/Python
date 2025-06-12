myList = [1,2,3,1]

print(myList.index(1)) #get the index of that value
myList.append(1) #append
print(myList)
myList.remove(1) #remove the value
print(myList)
lastValue = myList.pop() #remove the last value
print(myList)
myList.sort() #sort in ascending order
print(myList)
myList.reverse() #sort in descending order
print(myList)
print(len(myList)) #get the length
print(myList.count(1)) #how many time that number appear

# .index() .append() .remove() .pop() .sort() .reverse() len() .count()

for item in myList:
    print(item)
