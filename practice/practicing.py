print([1,2,3,4,5][1:4])

print([10,20,30,40,50][::-1])

for i in range(3):
    print(i,end=' ')
print()

print("hello".upper().replace("L","y"))

print("how are you?")

squares=[x**2 for x in range(5) if x%2==0]
print(squares)

d={'a':1,'b':2}
print(d.get('c',3))# 3 (here 3 is a default fallback)
# Note: It doesn't add 'c':3 to the dictionary, dictionary remains unchanged
# print(d['d']) #keyerror(because you didn't use get)
print(d.get('e'))# None(because here no default fallback)
print(d)
d.setdefault('f',6)#setdefault adds it to the dictionary
print(d)


def add(item,lst=[]):
    lst.append(item)
    return lst
add(1)
print(add(2))

a=[1,2,3]
b=a # Here it's not copying the list, both names point to the same object.
# use a.copy() or a[:] to make an actual copy
b.append(4)
print(a)

print(bool(0.0)) # False
print(bool([0.0])) # True

text="The cat is dancing. I am enjoying!"
def lower_text(text):
    text=text.lower().replace(".","").replace("!","")
    return text
print(lower_text(text))

# better alternatives for removing punctuations
# using str.translate with string.punctation
str1="How are you? I am not good. oh!"
import string
def punc(str1):
    punc=str1.lower().translate(str.maketrans("","",string.punctuation))
    return punc
print(punc(str1))

def greet(name):
    # return f"Hello, {name}!"
    # return "Hello "+name+"!"
    return "Hello, {}!".format(name)
print(greet("Asha"))

def is_even(n):
    if n%2==0:
        return True
    else:
        return False
print(is_even(4))
print(is_even(7))

numbers=[1,2,3,4,5,6]
def total(numbers):
    total_sum=0
    for num in numbers:
        total_sum+=num
    return total_sum
print(total(numbers))
print(total([10,20,30]))
print(total([]))

def largest(numbers):
    max_value=numbers[0]
    for num in numbers:
        if num>max_value:
            max_value=num
    return max_value
print(largest([13,29,7,44,20]))


def smallest(numbers):
    min_value=numbers[0]
    for num in numbers:
        if num<min_value:
            min_value=num
    return min_value
print(smallest([15,12,4,45,67,34]))
print(smallest([3,-5,-9,44,-17,4,33]))

def count_vowels(text):
    count=0
    vowels="aeiou"
    for char in text:
        if char.lower() in vowels:
            count+=1
    return count
print(count_vowels("Hello I am Avinash"))

# This is not the right way to do
def count_consonants(text):
    count=0
    vowels="aeiou"
    for char in text:
        if char.lower().replace(",","") not in vowels:
            count+=1
    return count
print(count_consonants("Hello I am Avinash, Let us build a project together"))


def reversed_text(text):
    clean_text=text.lower()
    reversed_str=""
    for char in text:
        reversed_str=char+reversed_str
    return reversed_str
print(reversed_text("Python"))


def is_palindrome(text):
    clean_text=text.lower()
    reversed_str=""
    for char in clean_text:
        reversed_str=char+reversed_str
    return reversed_str==clean_text
print(is_palindrome("Madam"))
print(is_palindrome("avinash"))


def get_evens(numbers):
    evens=[]
    for num in numbers:
        if num%2==0:
            evens.append(num)
    return evens
print(get_evens([1,2,3,4,5,6]))
print(get_evens([1,3,5]))


def factorial(n):
    result=1
    for i in range(1,n+1):
        result*=i
    return result
print(factorial(5))
print(factorial(1))
print(factorial(0))

def word_lengths(text):
    words=text.split()
    lengths=[]
    for word in words:
        lengths.append(len(word))
    return lengths
print(word_lengths("I love Python"))
print(word_lengths("hi"))

def greeting(name):
    return "Hello, {}!".format(name)
print(greeting("avinash avi"))

for i,value in enumerate(["a","b"],start=1):
    print(i,value)


dict1={"name":"avi","age":22,"city":"Bengaluru"}
for key in dict1:
    print(key)
# both are same we no need to explicitly mention for keys
for key in dict1.keys():
    print(key)

for value in dict1.values():
    print(value)

for item in dict1.items():
    print(item)


age=32
status="Major" if age>=18 else "Minor"
print(status)

print(type(0))#int


for j,value in enumerate(['a','b','c'],start=1):
    print(j,value)

m=[1,2,3,4,5]
print(m[::-1])
print(type(m))
m[0]=99
print(m)

n=(1,2,3,4,5,6)
print(id(n))
r=n[::-1]
print(id(r))

print(type(n))
# n[0]=77  # tuple object doesn't support item assignment
print(n)

for i in n:
    print(i)




