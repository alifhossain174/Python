friends = ["Fahim", "Alif", "Hossain"]

for friend in friends :
    print(f"{friend} is a part of my name")

grades = [35,52,14,56,98]
total = 0
amount = len(grades)

for grade in grades :
    total = total + grade

print(total)

# without using loop
average = int(sum(grades) / len(grades))
print(average)