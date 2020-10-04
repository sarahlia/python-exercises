#lambda function: doesn't have a name (but can be saved as a variable) and is only used to return values, not to perform actions.
#It's almost always a single line.
add = lambda x, y: x + y

print(add(5, 7))

#Example 1
def double(x):
    return x * 2

#Using list comprehension
sequence = [1, 3, 5, 9]
# doubled = [double(x) for x in sequence]
# print(doubled)

#Or instead, use map:
# If using map, we need to turn it into a list to print it out, because without it we'll just get a map object.
doubled = list(map(double, sequence))
print(doubled)

#Using lambda function:
doubled =[(lambda x: x * 2) (x) for x in sequence]
print(doubled) #but this is kind of unreadable, so..

#do this instead:
doubled = list(map(lambda x: x * 2, sequence))
print(doubled)




