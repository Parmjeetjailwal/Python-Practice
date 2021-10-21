# *args = parameter that will pack all arguments into a tuple
#        useful so that a function can accept a verying amount of arguments

def add(*stuff):
    sum = 0
    stuff = list(stuff)
    stuff[0] = 1
    for i in stuff:
        sum += i
    return sum

print(add(11,22,33,44,55,66))