numbers = [1, 3, 5]
doubled = [n * 2 for n in numbers]
print(doubled)

friends = ["Dee", "Faye", "Sasha", "Hannah", "Shane"]
starts_s = [friend for friend in friends if friend.startswith("S")]
new = ["Sasha", "Shane"]

# for friend in friends:
#     if friend.startswith("S"):
#         starts_s.append(friend)

print(starts_s)
print(starts_s is new) #false, they are different lists in memory, even though the elements are the same, as shown by the ids below:
print("starts_s: ", id(starts_s), "new: ", id(new))
print(friends[2] is starts_s[0]) #Sasha, so true

#If we want to make 2 lists the same:
new = starts_s
print("starts_s: ", id(starts_s), "new: ", id(new))
print(starts_s is new)



