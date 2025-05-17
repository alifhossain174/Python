class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Person Name is {self.name} and age is {self.age}"

person1 = Person("Fahim", 27)
print(person1)

        