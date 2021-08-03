#Loops.
#For loop.
#Use break for upto what we want.
#Use continue for what you dont want.
#If you want only a single digit to print use not equal in if.
even=[2,4,6,8,10,12,14,16,18,20]
print(type(even))
for i in even:
    if i==10:
        break
    print(i)
even=[2,4,6,8,10,12,14,16,18,20]
print(type(even))
for i in even:
    if i>10:
        continue
    print(i)
even=[2,4,6,8,10,12,14,16,18,20]
print(type(even))
for i in even:
    if i==10:
        continue
    print(i)
even=[2,4,6,8,10,12,14,16,18,20]
print(type(even))
for i in even:
    if i!=10:
        continue
    print(i)
