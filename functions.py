def ageInSeconds() :
    userAge = int(input("Type your age : "))
    ageInSeconds = userAge * 365 * 24 * 60 * 60
    responseString = f"Age in Seconds {ageInSeconds}"
    return responseString

print(ageInSeconds())