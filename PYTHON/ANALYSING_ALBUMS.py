import csv
with open('albumlist.csv','r') as csvfile:
    reader = csv.DictReader(csvfile)
    
    rows = 101
    for row in reader:
        rows =- 1
        if(rows > 0):
            print(row)
        else:
            break