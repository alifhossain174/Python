def multiplyNumbers(*args) :
    total = 1

    for arg in args :
        total = total * arg

    print(total)


multiplyNumbers(1,2)

def add(x, y) :
    return x+y

nums = [2,3]
print(add(*nums))