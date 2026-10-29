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
# data[0]=999
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
