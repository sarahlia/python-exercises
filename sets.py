friends = {"Bob", "Rolf", "Anne"}
abroad = {"Bob", "Anne"}

# gives the elements that are found in the first set, but NOT in the second set:
local_friends = friends.difference(abroad)
print(local_friends)
# the above can also be written as:
# print(friends - abroad)

jakarta = {"Anas", "Faye"}
seattle = {"Michelle"}

# gives the combination of the 2 sets:
buddies = jakarta.union(seattle)
print(buddies)
# the above can also be written as:
# print(jakarta | seattle)

art = {"Bob", "Jen", "Rolf", "Charlie"}
science = {"Bob", "Adam", "Jen", "Anne"}

# gives the common elements that are found in both sets:
both = art.intersection(science)
print(both)
# the above can also be written as:
# print(art & science)
