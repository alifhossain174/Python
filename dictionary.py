friendsAge = {"fahim":28, "nur":28, "sakib":30}

print(friendsAge["fahim"])
friendsAge["fahim"] = 24
print(friendsAge["fahim"])

friends = [
    {
        "name": "Md Fahim Hossan",
        "age": 27,
        "country": "Bangladesh"
    },
    {
        "name" : "Raihan Ahmed Nur",
        "age": 30,
        "country": "Bangladesh"
    }
]

print(friends[0]["name"])

for individual in friends :
    print(individual["name"])


for name, age in friendsAge.items() :
    if "fahim" in friendsAge :
        print(f"Name is {name} and age {age}")


my_dictionary = {'a': 1, 'b': 2, 'c': 3}
items = list(my_dictionary.items())
print(items)


my_dictionary = {'name': "Fahim", 'age': 28}
for key, value in my_dictionary.items():
    print(key, value)