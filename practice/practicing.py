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