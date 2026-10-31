with open("data.txt",'r') as r:
    # print(r.readlines()) # It gives all the data but in a single list with \n for every line
    # print(r.readline()) # It gives only the first line
    print(r.readline(2)) # It gives the first 2 characters 
    # print(r.read()) # It gives all the lines


with open("data.txt",'r') as r:
    data=print(r.readline())
    data=print(r.readline())
    data=print(r.readline())
    print(data)


with open("data.txt",'r') as r:
    for line in r:
        print(line.strip()) # strip() removes the trailing \n