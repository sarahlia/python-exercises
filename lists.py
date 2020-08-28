# can add or remove/modify elements from a list:
l = ["Ana", "Brinkley", "Candy"]

# canNOT be modified/add or remove elements from a tuple:
t = ("Ana", "Brinkley", "Candy")

# can add or remove elements from a set, but canNOT have duplicates in the set.
# the order is NOT guaranteed to be the same.
s = {"Ana", "Brinkley", "Candy"}

print(l[0])
print(t[1])

# since below is a set, it will generate an error when run:
# print(s[2])

l[0] = "Maggie"
print(l)

l.append("Korra")
print(l)

l.remove("Brinkley")
print(l)

# since below is a tuple, it will generate an error when run:
# t[1] = "Smith"
# print(t)

s.add("Smith")
s.add("Smith")
print(s)

