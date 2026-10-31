with open("append.txt",'a+') as f:
    f.write("This is number 1 line\n")
    f.write("This is number 2 line\n")
    print(f.tell()) # It tells the cursor position
    f.seek(0) # It brings the cursor to start
    print(f.read())

with open("append.txt","a+") as f:
    f.write('This is number 3 line\n')
    f.seek(0)
    print(f.read())