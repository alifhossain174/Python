myLists = [2,4,6]
doubledLists = []

for listitem in myLists :
    doubledLists.append(listitem*2)

print(doubledLists)

# but short way of doing it is which is called list comprehention
anotherDoubled = [x * 2 for x in myLists]
print(anotherDoubled)


friends = ["Sakib", "Nur", "Saad"]
friendNameWithS = []

for friend in friends :
    if friend.lower().startswith("s") :
        friendNameWithS.append(friend)

print(friendNameWithS)

# another way of doing it
friendNameWithSV2 = [friend for friend in friends if friend.lower().startswith("s")]
print(friendNameWithSV2)