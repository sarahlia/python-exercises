#dictionaries: connect keys and values

friend_ages = {"Minnie": 24, "Adam": 30, "Anne": 27}
print(friend_ages)
#to access, we must use the keys themselves, not the index:
print(friend_ages["Adam"])

friend_ages["Bob"] = 20
friend_ages["Minnie"] = 29
print(friend_ages)

#list of dictionaries, list is called friends:
friends = [
    {"name": "Mike", "age": 34},
    {"name": "Clyde", "age": 31},
    {"name": "Brian", "age": 29}
]
print(friends)
#to access the dictionaries in the list, we use index:
print(friends[0]["name"])
print(friends[0]["age"])


student_attendance = {"Cam": 96, "Bob": 80, "Anne": 100}
#get the keys:
for student in student_attendance:
    print(student)
#get the values:
for student in student_attendance:
    print(student_attendance[student])
#format the printout:
# for student in student_attendance:
#     print(f"{student}: {student_attendance[student]}% attendance.")

#A better way to access/print the above:
for student, attendance_percentage in student_attendance.items():
    print(f"{student}: {attendance_percentage}% attendance.")

if "Bob" in student_attendance:
    print(f"Bob's attendance is {student_attendance['Bob']}%")
else:
    print("That student does not exist in this class")

#If we want to find the average attendance:
values = student_attendance.values()
print( sum(values) /len(values) )