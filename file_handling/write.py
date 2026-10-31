# with open("write.txt",'w') as w :
#     w.write("Apple\n")
#     w.write("bason\n")
#     w.write("carrot\n")
#     w.seek(0)
#     print(w.read()) # not readable because we gave w not w+

with open("write.txt",'w+') as w :
    w.write("Apple\n")
    w.write("bason\n")
    w.write("carrot\n")
    w.seek(0)
    print(w.read().strip()) # It removes all white spaces
    w.seek(0)
    print(w.readline(3))
    # w.seek(0) without this it starts from the place where characters ended
    print(w.readline(),end="") # print adds its own newline so use end="" or strip() to avoid extra blank line
    print(w.readline())

print("It gives only the third line by discarding 1st and 2nd line")
with open("write.txt","r") as f:
    f.readline()
    f.readline()
    print(f.readline().strip())


# loop with enumerate()
with open("write.txt") as f :
    for number,line in enumerate(f,start=1): # by using start=1,we can start index at 1
        if number==3:
            print(line.strip())
            break