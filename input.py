# name = input("Enter your name: ")
# print(name)

size_input = input("How big is your house (in sq ft): ")
square_feet = int(size_input)
square_meters = square_feet / 10.8
print(f"{square_feet} sq ft equals {square_meters:.2f} sq m.")

user_age = int(input("Enter your age: "))
days = user_age * 365
print(f"Your age, {user_age}, is equal to {days} months.")
