friends = ["Omar", "Huraira", "Abdullah"]
if "abdullah" in friends :
    print("Yes")
else :
    print("No")

moviesWatched = {"Dhoom", "3 idiots", "Galaxy"}
watching = input("Which movie you are currently watching ? : ")

if watching in moviesWatched :
    print(f"{watching} Already Seen")
else :
    print(f"This {watching} is a New Movie")

# new code
magicNumber = [3,5,7]
userChoice = input("If you want to play then press 'y' : ").lower()

if userChoice == "y" :
    userInput = int(input("Type a Integer Number : "))
    if userInput in magicNumber :
        print("Your Guess is correct")
    else :
        print("You Guess a wrong Number")
else :
    print("oh ! you dont want to play")


