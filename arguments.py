def multiply(*args):
    # print(args)
    total = 1 #start with 1 saved as a variable named total
    for arg in args:
        total = total * arg #to multiply the arguments together

    return total

print(multiply(1, 3, 5)) #15
print(multiply(-1)) #-1
print(multiply(-2, 4)) #-8

def add(x, y):
    return x + y

nums = [3, 5]
print(add(*nums)) #the * will destructure the nums variable from the previous line. Without it, we'll get an error.

#We can also do this:
nums = {"x": 15, "y": 25}
print(add(**nums)) #It knows that ** means this is a dictionary with 2 keys.

#Special syntax: *args--collect all the positional arguments. operator--pass in a named argument at the end.
def apply(*args, operator):
    if operator == "*":
        return multiply(*args) #to separate out/unpack the tuple into individual values
    elif operator == "+":
        return sum(args)
    else:
        return "No valid operator provided to apply()"

print(apply(1, 3, 6, 7, operator="+")) #17
print(apply(1, 3, 5, 6, operator="*")) #90