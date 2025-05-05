myLists = ["Fahim", "Jebin", "Othoi"] # changable and ordered
myTuples = ("Bus", "Car", "Train") # non changable and ordered
mySets = {"Apple", "Banana", "Mango"} # changable, non ordered and unique item

myLists.append("asdasd")
print(myLists)
myLists.remove("asdasd")
print(myLists)

mySets.add("Pineapple")
mySets.add("Pineapple") #this item is already there so will not be added again becuase its a set
print(mySets)