# module
# a module is simply a python file(main.py) that contains code which can be reused in another program
# Built in : math,random,datetime,os etc
# Third party(installed with pip) : numpy,pandas,requests
# your own : any .py file you create

# import module
from math import sqrt
print(sqrt(49))
# print(cbrt(125)) # error because we just import sqrt from math

# import math as m(if you want short name)
import math
print(math.pi)
print(math.cbrt(125))
print(math.ceil(7.1)) #8
print(math.floor(7.7)) #7
print(math.pow(2,7))
print(math.e)
print(math.log(100,10))
print(math.lcm(18,6))
print(math.exp(5))

# import random
import random as rd
print(rd.random())
print(rd.randint(1,100))
print(rd.choice(["a","b","c"]))

import datetime as dt
now=dt.datetime.now()
print(now)

# import os
import os
print(os.listdir())
print(os.getcwd())
# print(os.mkdir("newfolder")) # create a new folder
# os.rename("old.txt","new.txt") #rename file

# import sys
import sys
print(sys.version)
print(sys.path)


# user defined modules
# you create your own .py file
# create file mymodule.py import it here
import mymodule
print(mymodule.greet("Trump"))