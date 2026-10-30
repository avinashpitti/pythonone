# function
# a function is a reusable block of code that performs a specific task.
# it runs only when called, it helps to avoid repetition and make code organized.
def greet():
    print("hello world")
    print("how are you doing?")

greet()

def invitation():
    return "how are you"
    return "my name is shivam" # It doesn't return
invitation()
a=invitation()
# print(invitation())
print(a)

def sum(a,b):
    print(a+b)
sum(2,3)

# parameters and arguments
#  parameters are the names in the definition 
#  arguments are the actual values you pass in

# return
# return sends a value back to the caller/program and exits the function
# a function without return gives back None
def wish(name):
    return f"Hello {name}"
print(wish("avinash")) #Hello avinash

def show():
    print("hi")
x=show()
print(x)  #None

# print only displays something on screen
# return hands the value back so you can store or reuse it

# sep(separator):By default print puts a space between items
# if you want specific separators it is useful
print(23,10,2026)
print(23,10,2026,sep='') #nospace
print(23,10,2026,sep='-')
print(23,10,2026,sep='/')

# end:By default print finishes with a newline,,so the next print starts on a newline
# end='' means don't move to the newline,
print('hello')
print('world')
print('hello',end='')
print('world')
print('hello',end=' ')
print('world')
print('hello',end='-')
print('world')
