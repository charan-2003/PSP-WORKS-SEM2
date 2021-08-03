students=["charan","suman","surya","praveen","arsh","ravi"]
student_info=["charan",10,9.5,"ECE",["chem","psp","maths"]]
print(type(students))
print(students)
print(type(student_info))
print(student_info)

#So in a list we can have strings, integer, float, another list in a list.
print(students[0])

#LIST SLICING
print(students[0:4])
print(students[:4])
print(students[2:-1])
print(students[0:-4])
print(student_info[-1])
print(student_info[-1][1])
print(student_info[-1][2])

#Appending list elements
students.append("venkat")
print(students)
#Appending will add the element i the last of the list.

#To replace any element from list

students[1]="anil"
print(students)
#This will replace any element in the list that we primarily have.

#To get the length of the list.
print(len(students))

#To remove any element from the list that we have.
students.pop(3)
print(students)

#To find the index value of an element in the list.
surya_index=students.index("surya")
print(surya_index)

#To print all the elements of list one-by-one.
for element in students:
    print(element)
