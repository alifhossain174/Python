def divisor(divident, divisor):
    return divident/divisor
    
try:
    print(int(divisor(10, 0)))  # This will print an error message
except ZeroDivisionError as e:
    print("Caught an exception:", e)
else:
    print("Division successful, no exceptions occurred.")