magicNumber = 7
userInput = input("If you want to play the Magic Number Game Press y/n : ").lower()

while userInput != "n" :
    userInputNumber = int(input("Press a number : "))
    if userInputNumber == magicNumber :
        print("Correct Number")
    elif abs(magicNumber - userInputNumber) == 1 :
        print("You are one Number behind")
    else : 
        print("Wrong Number")

    playAgain = input("Play again y/n : ").lower()
    if playAgain == "n" : 
        break