#string
name="avinash"
age=22
print(age)
print(type(age))
print(f"I am {name} {age} years old.")
age=str(age)
print(age)
print(type(age))

#int: it accepts all non-decimal numbers
num1=23
print(num1)
print(type(num1))

num2=-12
print(num2)
print(type(num2))

num3=0
print(num3)
print(type(num3)) 

#float:
a=1.0
print(a)
print(type(a))
b=-4.5
print(b)
print(type(b))

#list
info=["avinash",22,"vellore",3.5,[12,13,19,25],(1,2,3),{2,3,4,2,1},{"city":"Bengaluru","area":"marathahalli"}]
print(info)
print(type(info))
print(info[1])
print(info[::-1])
print(info[::2])
print(info[1::2])
print(info[4][1])
# print(info[5[2]])
# print(info[6[2]])
print(info*3)
print(info[5]*3)
print(info[-1])
# print(info[7][1])
info[0]="suresh"
print(info)

#Tuple
matter=1, # comma is what decides tuple not parantheses
print(matter)
print(type(matter))

data=(1,2,3,4,5,[1,2,3],{50,60,50,70})
print(data)
print(type(data))
print(data[4])
temp=list(data) # if you want to change the tuple first convert it into list
temp[0]=999
data=tuple(temp)
print(data)

#set
set1={1,2,1,1,3,5,"avinash","hyderabad","avinash"}
print(set1)
print(type(set1))
set2={1,10,20,30,40}
# print(set1+set2)
print(set2)
# set2[0]=33
print(set2)

#dict
dict1={
    "name":"avinash",
    "age":22,
    "address":{
        "h.no":"2-35",
        "street":"7th cross",
        "area":"karthika nagara",
        "city":"chennai"
    }
    
}
print(dict1)
# print(dict1[2])
print(dict1["address"])

dict2={
    "name":"varun",
    "age":22,
    "name":"kiran"
}
print(dict2)
print(type(dict2))
print(dict2["age"])
print("age:",dict2["age"])
print(f"age:{dict2['age']}")
print({"age":dict2["age"]})

for key,value in dict2.items():
    print(f"{key}:{value}")

for key in dict2.keys():
    print(key)

for key in dict2:
    print(key)

for value in dict2.values():
    print(value)

print("name" in dict2.keys())
print("varun" in dict2.values())

#immutable: whose value or state can't be changed after its creation
x=10
print(x)
print(id(x)) # different ids
x=20
print(x)
print(id(x))


numbers=[1,2,3,4]
# numbers.extend(789) # int objects are not iterable
numbers.extend('avinash') 
print(numbers)

numbs={1,2,3,4}
numbs.add(7)
print(numbs)

p=(3)
print(p)
print(type(p))
q=(4,)
print(q)
print(type(q))

# append,extend,add,update
digits=[1,2,3,4]
digits.append([5,6,7])
print(digits)
digits.extend([8,9])
print(digits)
digits.extend((10,20,30,40,50))
print(digits)

setadd={1,2,3,3,1,2,5}
print(setadd)
setadd.add(9)
print(setadd)
# setadd.update(10,20,30) # int object is not iterable
setadd.update('avinash')
print(setadd)