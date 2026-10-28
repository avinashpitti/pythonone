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

