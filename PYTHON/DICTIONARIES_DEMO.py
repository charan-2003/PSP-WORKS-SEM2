#This is about the dictionaries.
#A dictionary in python is the unordered and changable collection of data values that holds key value pairs.
#A dictionary in python is declared by enclosing a comma-seperated list of key-value pairs using curly braces.
#Curly braces are nothing but ({}).
#Syntax for python dictionary.

student1 = {'Name':'charan', 'branch':'ECE', 'section':'IOT', 'roll no':1}
print(type(student1))
print(student1)

student1 = {'Name':'charan', 'branch':'ECE', 'section':'IOT', 'roll no':1, 'Name':'surya'}
print(type(student1))
print(student1)
#so we got surya as output for Name so duplicating is not allowed in this dictionaries.
#To print any value in the dictionary.
print(student1['Name'])
print(student1['roll no'])

#To add any key value to a dictionary.
student1 = {'Name':'charan', 'branch':'ECE', 'section':'IOT', 'roll no':1}
print("Before updating")
print(student1)
#'member':'NCC'
student1.update({'member':'NCC'})
print("After updating")
print(student1)
#we can press tan key after pressing student1.up

#Delete keys from the dictionary.
#To delete any value from the dictionary.
student1 = {'Name': 'charan', 'branch': 'ECE', 'section': 'IOT', 'roll no': 1, 'member': 'NCC'}
print("Before deleting")
print(student1)
del student1['Name']
print("After deleting")
print(student1)

#PRINT(STUDENT1.ITEMS()) IF WE PRESS THIS IN IDLE WE GET THE LIST OF TUPLES IN DICTIONARY.
student1 = {'Name': 'charan', 'branch': 'ECE', 'section': 'IOT', 'roll no': 1, 'member': 'NCC'}
print("Keys of student1 are")
student1.keys()
print(student1.keys())

#To get values for the keys.
student1 = {'Name': 'charan', 'branch': 'ECE', 'section': 'IOT', 'roll no': 1, 'member': 'NCC'}
for i in student1.keys():
    print(student1[i])
student1.values()
print(student1.keys())
print(student1.values())
#You can use the student1.values also
