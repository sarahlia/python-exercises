number = 23

user_input = input("Would you like to play? (Y/n) ").lower()
while True:
    if user_input == "n":
        break

    user_number = int(input("Guess our number: "))
    if user_number == number:
        print("You are correct!")
        break
    elif abs(number > user_number) == 1:
        print("Go higher..")
    else:
        print("Go lower..")


friends = ["Jen", "Bob", "Anne", "Sam"]

for friend in friends: # or if we want numbers starting at index 0: for friend in range(4)
    print(f"{friend} is my friend.")


grades = [35, 67, 98, 100, 100]
# total = 0
size = len(grades)

# for grade in grades:
#     total += grade

# or instead of the commented lines above (line 25, 28, 29) we could do:
total = sum(grades)
print(f"The average is {total / size}")