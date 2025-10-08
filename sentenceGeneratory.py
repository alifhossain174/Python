import random

subjects = ["The cat", "A dog", "The president", "A scientist", "An artist"]
verbWords = ["jumps over", "runs to", "discovers", "paints", "analyzes"]
places = ["the fence", "the city", "a new planet", "a masterpiece", "data trends"]

def generate_headline():
    subject = random.choice(subjects)
    verbword = random.choice(verbWords)
    place = random.choice(places)
    return f"{subject} {verbword} {place}"

while True:
    print("Want to generate a random headline? (y/n)")
    user_input = input().strip().lower()
    if(user_input != 'y'):
        print("Goodbye!")
        break   
    else:
        print(generate_headline())