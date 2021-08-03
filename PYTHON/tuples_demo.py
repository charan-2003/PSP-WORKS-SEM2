#Tuples are identical lists in all respects, except for the following properties:
#1.Tuples are defined by enclosing the elements in parenthesis.
#2.Tuples are immutable

#Defing a tuple.
student=("charan","ramesh","ramu","tarak","tejas")
print(type(student))
for i in student:
    print(i)

student=("charan","ramesh","ramu","tarak","tejas")
#To print only tarak.
print(student[3])
#Student[3]= "anil" this will not work.
#So it cant changed to anil so tuples are immutable.
print(student[0:3])

#What are the benefits of using tuples instead of lists using python.
student=("charan","ramesh","ramu","tarak","tejas") #Tuple packing.
(s1,s2,s3,s4,s5)=student #Tuple un-packing.
print(s1)
print(student)
#student[s1]="amar" Now also tuple wont change.
print(s1)
print(s2)
print(s3)
print(s4)
print(s5)
#So by this we can print the elements individually

#(s1,s2,s3)=student
#shows error

#A tuple can have another tuple in it.
student=("charan","ramesh","ramu","tarak","tejas")
student_1=("charan","ramesh",("ramu","tarak","tejas"))
print(type(student_1))
print(student_1)
#To print ramu in student_1.
print(student_1[2][0])

#To swap s1 and s2 to names charan and ramesh.
(s2,s1,s3,s4,s5)=student
print(s1)
#Or
s3,s4=s4,s3
print(s4)
print(len(student))
print(len(student_1[2]))
