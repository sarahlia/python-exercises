# print statements
print(5 == (10/2))
print(5 > 5)
print(3 != 4)

# grouping
friends = ["Bob", "Anne"]
abroad = ["Bob", "Anne"]
new_list = friends

print(friends == abroad)

# The 'abroad' list is created in a new address in memory, so it's not the same as the 'friends' list.
# Hence 'is' is going to output 'False':
# print(friends is abroad)

#'friends' and 'new_list' are exactly the same list.
print(friends is new_list)

# =========================================================

day_of_week = input("What day of the week is it today?").lower()

# if day_of_week == "monday":
#     print("Have a great start to your week!")
# print("This msg has nothing to do with the if statement, so will always be shown.")

# running if statement :
if day_of_week == "monday":
    print("Have a great start to your week!")
elif day_of_week == "tuesday":
    print("It is Tuesday.")
else:
    print("At least the worst is behind you!")
    
# ===== Code Ended =====
