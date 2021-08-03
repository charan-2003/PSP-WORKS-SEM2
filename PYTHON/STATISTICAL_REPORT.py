import csv
with open('NetflixOriginals.csv','r') as csvfile:
    get_data = csv.DictReader(csvfile)

    print(get_data)
    print(type(get_data))
    print(get_data.fieldnames)

    for row in get_data:
        print(row)
        
    albums = []
    for row in get_data:
        albums.append(row)
        
    print("The number of albums are: ", len(albums))
    print(albums)
    print(type(albums))

