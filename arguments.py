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

########Part 2########
def named(**kwargs):
    print(kwargs)

named(name="Bob", age=25)


# def named(name, age):
#     print(name, age)
#
# details = {"name": "Bob", "age": 25}
#
# named(**details) #output: Bob 25

def print_nicely(**kwargs):
    # named(**kwargs)
    for arg, value in kwargs.items():
        print(f"{arg}: {value}")

print_nicely(name="Bob", age=25)


def both(*args, **kwargs):
    print(args)
    print(kwargs)

both(1, 3, 5, name="Bob", age=25) # 1, 3, 5 (positional arguments) will be collected into args; name="Bob", age=25 (named argument) will be collected into kwargs.


def myfunction(**kwargs):
    print(kwargs)
    # for arg, value in kwargs.items():
        # print(f"{arg} -- {value}")
# myfunction(**"Bob") #Error, must be mapping. Not a dictionary.
# myfunction(**None) #Error
myfunction(student="laura", grade=97) #This is ok.