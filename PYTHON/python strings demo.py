#In c we have character and group of character is string.
#In python we have no character only strings.
name1="charan"
print(name1)
print(type(name1))
name2='bharathi charan'
print(name2)
print(type(name2))
#So by the help of single quot also the string gets printed.

subject1='problem '
subject2='solving '
subject3='and '
subject4='programming '
subject=subject1+subject2+subject3+subject4
print(subject)
#Here use of '+' is used for concatenation.

#For slicing we use square brackets.
#To get only problem which have 6 letters or indexes includes o.
#We use [] and start index from 0 to n+1 so that 0 to 7.
print(subject[0:7])
print(subject[8:15])

#In operator will give you the membership.
print("solving"in subject)
#It is to check whether solving is there in subject are not.
print("Solving"in subject)
#If in word anything changed then it will give as false.

#Not in operator
print("semester" not in subject)
#It will tell if it is not there.
print("solving" not in subject)

#\n is for new line to output.
print("\nprints \n")
#If we put r before output in print we get all symbols in output with \n also.
#It is known as raw operator which means it print all characters.
print(r"\nprints \n")
print(R"\nprints \n")
#So we can use r and R for raw operator.

#%s string format.
#%d is for integer format.
sub='maths'
part=1
print("%s%d"%(sub,part))
print("We have part %d of %s subject in the first semester"%(part,sub))


#Repeat (*) operator.
print(subject1*3,subject2*3,subject3*3,subject4*3)
#It will repeat the specific string into ntimes in same line.
print((subject1+" ")*3)
#If we want in upper case.
print(subject1.upper())
#For lower case.
print(subject1.lower())

sentence="PSP is my favourite subject"
print(sentence)
print(sentence.split(' '))
