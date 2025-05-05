friends = {"Saad", "Nur", "Sakib", "Fahim"}
abroadFriends = {"Sakib", "Fahim"}
localFriends = friends.difference(abroadFriends)
allFriends = friends.union(abroadFriends)
print(localFriends)
print(allFriends)

science = {"Fahim", "Sakib", "Nur", "Saad"}
commerce = {"Nur", "Saad"}
common = science.intersection(commerce)
print(common)