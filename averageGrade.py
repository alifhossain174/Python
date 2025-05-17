student = {"name" : "rolf", "grades" : [100,99,95,90,88]}

def average(sequence) :
    return sum(sequence) / len(sequence)

print(average(student["grades"]))