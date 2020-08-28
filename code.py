# x = 15
# price = 9.99
#
# discount = 0.2
#
# result = price * (1 - discount)
#
# print(result)
#
# name = "Rolf"
#
# print(name * 2)

# a = 25
# b = a
# print(a)
# print(b)
#
# b = 17
#
# print(a)
# print(b)

person = "Rona"
phrase = f"Welcome, {person}!"
print(phrase)

name = "Bob"
greeting = "Hello, {}"
with_name = greeting.format(name)
with_anothername = greeting.format("Rolf")
print(with_name)
print(with_anothername)

longer_phrase = "Hello, {}. Today is {}."
formatted = longer_phrase.format("Sarah", "Thursday")
print(formatted)


