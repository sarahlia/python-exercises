#brackets are not needed for straight up tuples.
t = 5, 11
x, y = t
print(x, y)

student_attendance = {"Cam": 96, "Bob": 80, "Anne": 100}
print(list(student_attendance.items()))

# for student, attendance_percentage in student_attendance.items():
#     print(f"{student}: {attendance_percentage}% attendance.")

for el in student_attendance.items():
    print(el)

people = [("Bob", 42, "mechanic"), ("James", 24, "painter"), ("Harry", 32, "lecturer")]

for name, age, job in people:
    print(f"The person named {name} is {age} years old and works as a {job}.")

#alternatively, the above can also be written as:
for person in people:
    print(f"The person named {person[0]} is {person[1]} years old and works as a {person[2]}.")

#The convention is that if you use an underscore, that variable is to be ignored (42 in the case below):
person = ("Bob", 42, "mechanic")
name, _, job = person
print(name, job)

#if we want to separate the list [1, 2, 3, 4, 5] into 2 lists: 1 with only the first element and another with the rest:
head, *tail = [1, 2, 3, 4, 5]
print(head)
print(tail)

#if we want to separate the list [1, 2, 3, 4, 5] into 2 lists: 1 with the tail only and another with all the other elements:
*head, tail = [1, 2, 3, 4, 5]
print(head)
print(tail)