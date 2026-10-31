# csv is a comma separated values.Each line is a row,and commas separate the columns.

import csv

with open("students.csv",'w',newline='') as f :
    writer=csv.writer(f)
    writer.writerow(["name","marks","city"])
    writer.writerows([
        ['varun',88,'chennai'],
        ['santhosh',79,'hyderabad'],
        ["arun",99,'bengaluru']
    ])

with open("students.csv",'r') as f:
    reader=csv.reader(f)
    header=next(reader)
    print(header)
    for row in reader:
        print(row)


with open("students.csv",'a') as f:
    csv.writer(f).writerow(['srinivas',92,'nalgonda'])

with open("students.csv",'a+') as f:
    csv.writer(f).writerow(['vasanth',88,'vijayawada'])
    f.seek(0)
    reader=csv.reader(f)
    header=next(reader)
    print(header)
    for row in reader:
        print(row)