'''append elements (key , value),
key:priority
value:element in queue
and sort the list every time an element is suspended'''

students_grade=[]

students_grade.append((1,"Akash"))

students_grade.append((4,"Ankitha"))

students_grade.sort(reverse=True)
print("Yes")
print(students_grade)

students_grade.append((3, "sid"))
students_grade.sort(reverse=True)
students_grade.append((2,"akshay"))
students_grade.sort(reverse=True)
print("priority wise sorted")
print(students_grade)
print("original queue")
while students_grade:
    print(students_grade.pop())
