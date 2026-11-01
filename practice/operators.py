print(5 and 10 and 7) # if all true, last truth in and case
print(5 or 10 or 7) # if all true, first true in or case

x=700000
y=700000
print(x is y)

# ternary 
n=9
result="even" if n%2==0 else "odd"
print(result)

print([1,2]+[3,4])
print(1*5)
print(1**5)
print([1]*5)

print(-7//2,-7%2,7//-2,7%-2)
print( 0 or "" or "hello")
print( 5 and 0 and 10)
print([] and "x" or "y")

x=10
res=x>5 and x<20 or x==100
print(res)

s=None
print(s is None)
print(s==None)

print("************************")
data="programming"
if(length:=len(data))>8:
    print(f"Long word:{length}")
else:
    print("short word")


print(False and True or 10 and False)

print(-13 // 4, -13 % 4)
print(13 // -4, 13 % -4)
print(-13 // -4, -13 % -4)
print(2 ** -1, 2 ** 0.5)

print(7.5 % 2)
print(-7.5 % 2)
print(7.5 // 2)
print(10 % 3.5)

x = 6
print(x & 1 == 0)
print((x & 1) == 0)

y = 4
print(y | 1 == 5)
print((y | 1) == 5)

def f(x):
    print(f"called {x}")
    return x

result = f(0) and f(1) or f(2)
print("result:", result)

n=15
p=7
q=12
s="cat"

res1=True if n%2==0 else False
print(res1)

res2=True if n%3==0 or n%5==0 else False
print(res2)

res3= p if p>q else q
print(f"The larger of two numbers p and q {res3}")

res4=True if "a" in s and len(s)>3 else False
print(res4)

print("******************")

e = None
print(e is None and e == None)
print(None is None is None)

print(8>>1<<3) #32(right shift divide by 2**value,left shift multiply by 2**value)

total = 0
data = [0, 5, 0, 7, 0, 3]

for v in data:
    if (total := total + v) > 10:
        print(f"Threshold hit at {v}, total={total}")
        break
print("Final:", total)


a = 7
b = 2
c = 3

result = (
    a % b == 1
    and (a * b > c ** 2 or not (c & b == 2))
    or (a >> 1) ^ b == 1
)
print(result)

print(7>>1^2==1)


count=0
for x in [1,2,3,4]:
    if x%2==0:
        pass
        count+=10
    count+=1
print(count)

print(3>2 and 5<10)
print(5<3 or 5<3)

print(10 & 20)
print(10 or 20)

n=0
status= "positive" if n>0 else "negative" if n<0 else 'zero'
print(status)

x=10
while x>0:
    x-=3
print(x)

# walrus operator(:=)
print(w:=9) #it directly assigns the value to a variable and returns it
print(x:=7)

x=[5,7]
print( 5 in x)
print( 5 is x)

a=[1,2]
b=a
a+=[3]
print(a,b)

a=a+[4]
print(a,b)

x=[2,3,4]
y=x[:]
print(y)

p=[]
q=[]
print(p is q)

age=121
final="major" if age>12 else "minor"
print(final)

print(not 0)
print(not True)

