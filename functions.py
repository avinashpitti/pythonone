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

# def sum(a,b):
#     print(a+b)
# sum(2,3)

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


# types of arguments
# positional,keyword,default,*args,**kwargs
# positional arguments: matched by order
def student(name,age=21):
    return name,age
print(student("avinash",22))
# print(student(32,"avinash"))

# keyword arguments: matched by name,so order doesn't matter
print(student(age=19,name="suresh"))

# default arguments: used when no value is passed
print(student(name="anil"))

# *args: any number of positional args collected as a tuple
def total(*args):
    print(args)          # (1, 2, 3)
    return sum(args)

print(total(1, 2, 3))           # 6

# **kwargs : any number of keyword arguments(collected as a dictionary)
def show(**kwargs):
    print(kwargs)
show(name='kiran',age=22)

# scope: where a variable can be accessed
x=20 # global
def test():
    y=5 # local
    print(x,y)
test()
print(x) #20
# print(y) # error: name y is not defined

# lambda:a one line anonymous function
# often used map,filter,sorted
cubed=lambda c:c**3
print(cubed(6))

# map: applied function to each item
nums=[1,2,3,4,5,6,7,8,9]
sqs=list(map(lambda s:s**2,nums))
print(sqs)

# filter(): keeps items where function returns True
evens=list(filter(lambda f:f%2==0,nums))
print(evens)

# sorted
numbers=[45,23,18,33,99,5,78,20]
sorting=sorted(numbers)
print(sorting)