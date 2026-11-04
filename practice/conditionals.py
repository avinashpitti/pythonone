age=89
if age>18:
    print("Major")
x=7
# Version A
if x > 0:
    print("positive")
if x < 0:
    print("negative")

# Version B
if x > 0:
    print("positive")
elif x < 0:
    print("negative")


if "False":
    print("truthy")
else:
    print("falsy")