def hello():
    print("Hello!")

hello()
# hello("Bob") #won't work

# def user_age_in_seconds():
#     user_age = int(input("Enter your age: "))
#     age_seconds = user_age * 365 * 24 * 60 * 60
#     print(f"Your age in seconds is {age_seconds}")
#
# print("Welcome to the 'Age in Seconds' program!")
# user_age_in_seconds()
#
# print("Goodbye!")

#Another example
friends = []
def add_friend():
    friends.append("Marcy")

#This will add Marcy multiple times
add_friend()
add_friend()
add_friend()

print(friends)

#pass means do nothing
def add(x, y):
    result = x + y
    print(result)

add(5, 3)

def say_hello(name, last_name):
    print(f"Hello, {name} {last_name}!")

say_hello(last_name="Jordan", name="Michael") #still works as we intended, because we put the argument keywords before the values.
#In Python there's usually no space between the argument keyword and the value.

def divide(dividend, divisor):
    if divisor != 0:
        print(dividend/divisor)
    else:
        print("You fool, you can't do that!")

divide(24, 8)#this is called positional arguments--the order matters.
divide(15, 0) #can also be written as keyword arguments like this: divide(dividend=15, divisor=0)

divide(56, divisor=8)#we can do this,
# divide(dividend=39, 3)#but we CAN'T do this, as positional argument has to go first. This rule goes for parameters too.

#Use keyword arguments whenever possible to be really clear(unless it's really obvious).

def sum(x, y=8):
    print(x + y)

sum(5) #this is the same as saying: sum(x=5)

#This won't work:
# sum(y=5)

#This works too:
sum(x=5, y=7)

#We can do this:
default_y = 3

def add(x, y=default_y):
    sum = x + y
    print(sum)

add(2)

#The second parameter in line 70 only works within that function, not oustide it:
default_y = 4
add(2) #the result stays the same, because we are using the value from line 68.

