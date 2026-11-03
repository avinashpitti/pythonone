s="hello"
s2=s
s+="world"
print(s,s2)

a=[1,2]
b=a
a.append(3)
print(a,b)

t=(1,[2,3])
t[1].append(4)
print(t)

t2=(1,[2,3])
# t2[1]=[9,9]
print("done")

print(3+4.0)
print(3+True)
print(True+True+True)
print("3"+"4")
# print("3"+4) str+int cant concatenate
print(3*"ab")
print([1]*3)
print([1,2]+[3])
print("ab"*2+"c")
print(True+False+True*False)

print(type(5)==int)
print(type(True)==int)
print("*********isinstance*********")
print(isinstance(True,int))
print(isinstance("hi",int)) #"hi" is a str,not an int
print(isinstance("hi",str))
print(isinstance(5,object))
print(isinstance(True,bool))
print(isinstance(True,(int,float)))


t3=tuple([1,2])
print(type(t3))

t5=1,2,3
print(type(t5))

print(type({}))
print(type(set()))

print({1,2}&{2,3})
print({1,2}-{2,3})
print({1,2}^{2,3})


print("*******dict***********")
d = {"a": 1, "b": 2}
print(d["a"])
print(d.get("c"))
print(d.get("c", 0))
print("a" in d)
print(list(d.keys()))
print(list(d.values()))
print(list(d.items()))
print(len(d))
# print(d["c"])         # uncomment — what happens?
# print(d[[1, 2]])      # uncomment — what happens?

s="hello"
print(s.upper())
print(s)
s=s.upper()
print(s)

print(round(0.1+0.2,1)==0.3)
print(1_000_000)
print(-0.0==0.0)

print(5//2.0)
print(divmod(17,5))
print(abs(-5),abs(-5.5))
print(int(3.9))
print(round(3.5),round(2.5))
print(1_22)
print(abs(5.2))
print(int("10")+3)
print(int(-3.9))

import copy

a = [1, 2, [3, 4]]
b = a                # alias
c = a[:]             # shallow copy
d = copy.deepcopy(a) # deep copy

a[2].append(5)       # mutate inner list

print(a)
print(b)
print(c)
print(d)

a.append(99)
print(a)
print(b)
print(c)
print(d)


print("print all these")
print(int("42")) #42
print(int("  42  "))#42
print(float("3.14"))#3.14
print(str(42))#"42"
print(list("abc"))#['a','b','c']
print(tuple([1, 2]))#(1,2)
print(set([1, 2, 2, 3]))#{1,2,3}
print(list(range(3)))#[0,1,2]
print(bool(""))#False
print(bool("0"))#True
print(bool(0))#False
print(bool([]))#False
print(bool("False"))#True


# squence type comparison
print("sequence type comparison")
print("abc"[1]) #b
print(("a", "b", "c")[1])#b
print(["a", "b", "c"][1])#b
print(range(5)[1])#1
print("abc"[1:])#bc
print(("a", "b", "c")[1:])#('b','c')
print(["a", "b", "c"][1:])#['b','c']
print(range(5)[1:])#(1,5)


#None behaviour
print("None behavior")
print(type(None))#None
print(None == None)#True
print(None is None)#True
print(bool(None))#False
x = None
print(x is None)#True
print(x == None)#True
print(None == 0)#False
print(None == False)#False
print(None == "")#False

print("understand isinstance")
print(isinstance(True, int))#True
print(isinstance(True, bool))#True
print(isinstance(5, bool))#False
print(isinstance(5, object))#True
print(type(True) == int)#True
print(type(True) == bool)#True

# Numeric tower:
print(isinstance(5, (int, float)))#True
print(isinstance(5.0, (int, float)))#True
print(isinstance(True, (int, float)))#True