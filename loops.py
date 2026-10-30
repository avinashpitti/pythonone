# loops
# loops are used to execute a block of code repeatedly until a condition is met

# for loop
# a for loop iterates over a sequence and execute the block for each item
for char in "python":
    print(char)

for i in range(10):
    print(i)

info="This is for loop"
for info in info:
    print(info)

# range() function
# range generates a sequence of characters

# while loop
# while loop runs as long as condition is true
i=5
while i>=1:
    print(i)
    i-=1

# infinite loop
# a loop that never becomes false
# while True:
#     answer=input("Type 'quit' to exit : ")
#     if answer=='quit':
#         break

# break immediately exits the loop when encountered
# continue skips the current iteration and moves to the next one
i=100
while i>90:
    i-=1
    if i==96:
        continue
    if i==93:
        break
    print(i)


for i in range(10):
    if i==4:
        continue
    if i==7:
        break
    print(i)


# for-else while-else
# The else block runs only if the loop finished without hitting break
for i in range(5):
    print(i)
else:
    print("loop finisehd")

for j in range(6):
    if j==3:
        break # here it hit break so else block doesn't run
    print(j)
else:
    print("loop finisehd")

# nested loop
# a loop inside another loop.inner loop runs completely for each iteration of outer loop
for outer in range(3):
    for inner in range(4):
        print(outer,inner)

# enumerate
# enumerate gives both index and value while looping
fruits=["apple","banana","cherry","dragon"]
for fruit in fruits:
    print(fruit)

for index,fruit in enumerate(fruits,start=1):
    print(index,fruit)

for index,fruit in enumerate(fruits,start=1):
    print(f"{index} : {fruit}")


# zip
# zip combines two or more iterables together for parallel looping
names=["alice","bob","charlie","deng"]
scores=[67,84,52,90]
for name,score in zip(names,scores):
    print(name,score)

# list comprehension
# a concise way to create lists using a loop in one line
squares=[i**2 for i in range(1,6)]
print(squares)
# normal way
cbs=[]
for i in range(1,6):
    cbs.append(i**3)
print(cbs)
