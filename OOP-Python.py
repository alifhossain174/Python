class Student :
    def __init__(self, name, grades):
        self.name = name
        self.grades = grades

    def average(self):
        return sum(self.grades)/len(self.grades)


student = Student("MD Fahim Hossain", [50,100])
print(f"{student.name}'s average grade is {student.average()}")