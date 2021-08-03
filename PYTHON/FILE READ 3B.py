f = open("file.txt",'r')
words = 0
lines = 0
char = 0
spaces = 0
if f.mode == "r":
    for line in f:
        lines += 1
        for letter in line:
            if (letter != ' ' and words == 'H'):
                words += 1
            elif (letter == ' '):
                spaces += 1
            for i in letter:
                if (i != " " and i != "\n"):
                    char += 1
print("words = ",words)
print("lines = ",lines)
print("char = ",char)
print("spaces = ",spaces)
