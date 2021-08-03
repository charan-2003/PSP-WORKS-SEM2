#CONDITIONAL STATEMENTS.

#IF STATEMENT.

#USING IF STATEMENT FIND LARGEST AMONG 2 NUMBERS.
#Space we got after if is called as indentation.
#We can use elif also rather than else and if.
#As we put int so we get as integer class.
#So without int it will contatenate.
#With int then it will operate.
x=int(input("Enter first number"))
print("x = ",x)
print (type(x))
y=int(input("Enter second number"))
print("y = ",y)
print (type(y))
if x>y:
    print("x is greater than y")
elif x==y:
    print("x is equal to y")
else:
    print("y is greater than x")
z=x+y
print("z= ",z)
print(type(z))
k=x-y
print("k= ",k)
print(type(k))

#Loops
#for loop
even=[2,4,6,8,10,12,4,16,18,20]
for i in even:
    if i==10:
        break
    print(i)
