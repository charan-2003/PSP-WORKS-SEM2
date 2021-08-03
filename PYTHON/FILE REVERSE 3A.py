file = open("output_data.txt", "w")

with open("file_data.txt", "r") as myfile:
    data = myfile.readlines()
    rev_data = data[::-1]
    file.writelines(rev_data)
    print(rev_data)
if file.mode=="r":
    contents = file.read()
    print(contents)
    print(len(contents))
    print(type(contents))

file.close()
