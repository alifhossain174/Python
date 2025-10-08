import os
HISTORY_FILE = "history.txt"

def fileCheck():
    if not os.path.exists(HISTORY_FILE):
        open(HISTORY_FILE, "w").close()

def showHistory():
    fileCheck()
    historyFile = open(HISTORY_FILE, "r")
    contents = historyFile.readlines()
    historyFile.close()
    if len(contents) > 0:
        fileHistoryText = ''
        for content in contents:
            fileHistoryText = fileHistoryText + content
        return fileHistoryText
    else:
        return "No History Found!"
    
def clearHistory():
    fileCheck()
    os.remove(HISTORY_FILE)
    return "Hisotry Removed"

def calculation():
    fileCheck()
    userGivenInput = input()
    operators = ['+', '-', '*', '/']
    for op in operators:
        if op in userGivenInput:
            num1, num2 = userGivenInput.split(op)
            num1 = float(num1)
            num2 = float(num2)
            resultString = ""
            if op == '+':  
                result = num1+num2
                resultString = f"{num1}+{num2}={result}"
            elif op == '-':
                result = num1-num2
                resultString = f"{num1}-{num2}={result}"
            elif op == '*':
                result = num1*num2
                resultString = f"{num1}*{num2}={result}"
            elif op == '/':
                result = num1/num2
                resultString = f"{num1}/{num2}={result}"
            else:
                return "Invalid operator"

            historyFile = open(HISTORY_FILE, "a")
            historyFile.write(f"{resultString}\n")
            historyFile.close()
            return resultString


while True:
    print("Select Option: calculate/history/clear/close ")
    userInput = input().strip().lower()
    if userInput == 'history':
        print(showHistory())
    elif userInput == 'clear':
        print(clearHistory())
    elif userInput == 'calculate':
        print("Write your calculation like 123+456")
        print(calculation())
    else:
        print("GoodBye")
        break
