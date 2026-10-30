# Exception handling
# Exception handling is used to handle runtime errors so the program doesn't crash
# It allows program to continue running even if an error occurs.

# basic handling:
try:
    x1=int(input("Enter a number x1 :"))
    print(10/x1)
except:
    print("something is wrong")

# try:code that might fail
# except: runs only if an error occurs in the try block
# a bare except is a bad practice, catch specific error instead

# catching specific exceptions
try:
    x=int(input("Enter a number :"))
    print(10/x)
except ValueError:
    print("please enter a valid number")
except ZeroDivisionError:
    print("cannot divide by zero")
finally:
    print("Always runs no matter what")


# Raising exception:
# sometimes you want to create an error on purpose if certain conditions are not met.
#  you use the raise keyword
age=-5
if age<0:
    raise ValueError("Age can't be negative!")