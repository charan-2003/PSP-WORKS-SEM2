#File handling in python

f=open("file.txt","r")

if f.mode=="r":
    contents = f.read()
    print(contents)
    print(len(contents))
    print(type(contents))
#When text file is in same folder dont need to type full path simply filename.txt is enough.

#a means to append.


f=open("file.txt","a+")
f.write("i am 17 year old")
f=open("file.txt","r")
if f.mode=="r":
    content = f.read()
    print(content)
f.close()
#f.close is for closing the file.


f = open("file.txt","w")
if f.mode=="w":
    f.write("I lives in visakhapatnam")
f.close()
#For writing in file use "w".
