# Built in functions:
# Built in functions are functions that come ready-made with python.
# you can use them anywhere without importing anything

# 1)input/output
# print:displays output
# input: takes input(always returns a string)

# 2)type conversion
# int,float,bool,str,list,tuple,set,dict
print(dict(a=1,b=2)) #{'a': 1, 'b': 2}

# 3)math and nums
nums=[4,9,1,7]
print(len(nums))
print(sum(nums))
print(max(nums))
print(min(nums))
print(abs(-10))
print(pow(7,3))
print(divmod(19,5)) # 3 is a quotient,4 is a remainder
print(round(54.55553,2))


# 4)sequences and iteration
data=[4,9,1,7]
# sorted is a built in funtion, .sort is a list method
print(sorted(data))
print(list(reversed(data)))
print(list(range(3)))
print(list(enumerate(['a','b','c'])))
print(list(zip([1,2],['x','y'])))

# map,filter,any,all
info=[1,2,3,4,5]
print(list(map(lambda x:x**3,nums)))
print(list(filter(lambda y:y%2==1,nums)))
print(any(x>3 for x in info))
print(all(x>3 for x in info))


# type checking and inspection
print(type(5))
print(isinstance(7,int))
print(id(nums))
print(dir(nums))
print(help(len))


# characters and number systems
print(ord('A'))
print(ord('a'))
print(chr(66))
print(bin(10))
print(oct(10))
print(hex(255))

# others
# callable,len,eval,open etc
print(len("avinash"))