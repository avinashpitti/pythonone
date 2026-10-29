# condtional statements
# condtional statements allow the program to make decisions and execute different 
# blocks of code based on whether a condition is true or false

# if statement
# It executes a block of code only if the condition is true
age=34
if age>18:
    print("Major")

# if else
#  it chooses between two
if age>18:
    print("Major")
else:
    print("Minor")

# nested if
# an if statement inside another if statement
if age>18:
    if age>60:
        print("senior citizen")
    else:
        print("Just an adult")


# if elif else
# It chooses among three or more
marks=82
if marks>80:
    print("A grade")
elif marks>65:
    print("B grade")
elif marks > 50:
    print("C grade")
elif marks>40:
    print("D grade")
else:
    print("E grade")

# Ternary operator
# a shorthand way to write if else in a single line
status="adult" if age>18 else "minor"
print(status)

# match statement
# It is a python's version of switch case statement we find in other languages

status=404
match status:
    case 200:
        print("success")    
    case 404:
        print("page not found")
    case 500:
        print('server error')
    case _:
        print("unknown status")
