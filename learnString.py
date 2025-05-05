
# f string
fullName = "Md Fahim Hossain"
greetings  = f"Hello {fullName}"
print(greetings)
fullName = "Jobdaida Yasmin"
greetings  = f"Hello {fullName}"
print(greetings)

# using format
customerName = "Mohammad Fahim"
greetingTemplate = "Hello {}"
finalGreeting = greetingTemplate.format(customerName)
print(finalGreeting)

# long template using format
longerTemplate = "Hello {}, Today is {}"
finalTemplate = longerTemplate.format("Fahim", "Sunday")
print(finalTemplate)