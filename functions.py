def hello():
    print("Hello!")

hello()

def user_age_in_seconds():
    user_age = int(input("Enter your age: "))
    age_seconds = user_age * 365 * 24 * 60 * 60
    print(f"Your age in seconds is {age_seconds}")

print("Welcome to the 'Age in Seconds' program!")
user_age_in_seconds()

print("Goodbye!")

#Another example
friends = []
def add_friend():
    friends.append("Marcy")

#This will add Marcy multiple times
add_friend()
add_friend()
add_friend()

print(friends)
