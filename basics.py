print("Hello world!")

f_name="avinash"
print(len(f_name))
print(f_name[2])
print(type(f_name))

nums=[1,2,3,[4,5]]
print(len(nums))
print(nums[3]) #[4,5]
nums.append(6)
print(nums)
nums.pop()
print(nums)

print("difference between is and ==")
a=[2,3]
b=[2,3]
c=a
print(a is b)
print(a is c)
print(a==b)
print(a==c)
print(id(a))
print(id(b))
print(id(c))

# city=input("Enter your city:")
# a=int(input("Enter your marks:"))
# b=int(input("Enter your marks:"))

# hashable
# an object is hashable if its hash value never changes during its lifetime
# It can be compared to other objects with ==
print(hash("avinash"))
print(hash(22))

# shallow copy
# a shallow copy creates a new outer object,but inner objects still share the same memory
a=[1,2,3]
b=a
b[0]=99
print(a)
print(id(a))
print(id(b))

c=[10,20,[30,40]]
d=c
d[2].append(50)
print(c)
print(d)
print(id(c))
print(id(d))


#  deep copy
# deep copy creates new outer objects, and new inner objects
# completely independent
# we have to import copy

import copy
m=[[1,2],[3,4]]
n=copy.deepcopy(m)
m.append(99)
print(m)
print(n)
print(id(m))
print(id(n))

s=[3,4,5,6]
t=copy.deepcopy(s)
s.append(999)
print(s)
print(t)
print(id(s))
print(id(t))
# print(hash(s))
# print(hash(t))


p=[1,2,3,[4,5]]
q=copy.deepcopy(p)
q.append(777)
print(p)
print(q)

