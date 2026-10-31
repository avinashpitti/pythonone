import os 

if os.path.exists("append.txt"):
    print("file found")

try:
    with open("missing.txt") as f:
        print(f.read())
except FileNotFoundError:
    print("file not found")
except PermissionError:
    print("No permission to open this file")


# os.remove("append.txt")  # delete a file
# os.rename("append.txt","appends.txt") # rename a file

        