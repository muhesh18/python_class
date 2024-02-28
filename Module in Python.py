#Modules in Python :
#---------------------

'''Modules are pre-written pieces of code that are used to perform common tasks
like generating random numbers,performing mathematical operations

Python module is a file that contains some definitions and statements.when a
python file is executed directly,it is considered the main module of a progarm


#Math Module - It is used for Mathematical Calculations

#help - it is a keyword like dir 

print(help('math'))

print(help('keywords'))

print(dir('math'))

#-------------------------------

import math             #This is one type of import module
print(math.sqrt(81))    #This is one Package

import math as m                            #This is another type of import module
n=int(input("Enter the Number : "))
print("Square Root of N is : ",m.sqrt(n))

n=int(input("Enter the Number : "))
print(f'Factorial of {n} is {m.factorial(n)}')

from math import *                #This is another type of import module in which we don't use math keyword while calling packages...
print(ceil(45.1))              #ceil means next to point(right side of point)
print(floor(45.09))            #floor means before to point

print("Remainde Value is :",remainder(45,2))   #It will give the Remainder...
print("GCD is :",gcd(24,12))

#Trignometric Functions :
#-------------------------

from math import *
print("Sine Value is :",sin(0))
print("Cosine Value is :",cos(0))
print("Tan Value is :",tan(0))

#Logarithemic Functions :
#--------------------------

print(log(6))
print(log2(5))
print(log10(4))

#Constant Functions :
#--------------------

print("pi Value is :",pi)
print("Euler Number is :",e)
print("Tau Value is :",tau)

from math import *
r=int(input("Enter the Number : "))
print("Square value is : ",pi*r**2)

print("Not a Number : ",nan) #nan means - Not a Number
print("Infinity is : ",inf)  #inf means - infinity

#cmath - Complex Mathematical :
#-------------------------------

import cmath as c     #Real and Imaginary part
print(c.sqrt(49))

#Calendar Module :
#------------------

import calendar
print(calendar.calendar(2024))

import calendar as cal
year=int(input("Enter the year : "))
print(cal.year('year'))

year=int(input("Enter the Year = "))
month=int(input("Enter the Month = "))
print(calendar.month(year,month))

print(dir(calendar))

import calendar as cal
y=int(input("Enter the Year = "))
if(cal.isleap(y)):
    print(y,'is a Leap Year..')
else:
    print(y,'is not a Leap Year')

import calendar
print(calendar.calendar(2024,4))     #4 makes the spacing inbetween two months...
'''

#Date Time Module :
#-------------------

from datetime import date        #datetime is a module... date is a package
today=date.today()
print(today)

print(today.year)       #today is a function...
print(today.day)
print(today.month)

import datetime
today=datetime.datetime.now()
print(today)

date=datetime.date(2012,12,25)    #date(function)
print(date)

from datetime import datetime
now=datetime.now()
t=now.strftime("%H:%M:%S")    #strf(String Format)
print(t)

now=datetime.now()
t=now.strftime("%M:%D:%Y,%H:%M:%S") #%M-min, %D-Date, %Y-year, %H-Hour,
print(t)

now=datetime.now()
t=now.strftime("%m:%B:%y")  #(small m is month in Number) and (B is Month in letter but in small b it will give short form of month) and (small y is year in short form)
print(t)

now=datetime.now()
t=now.strftime("%m:%b:%y")
print(t)
t=now.strftime("%d----%a-----%y----%x----%X")
print(t)
t=now.strftime("%C------%c------%x------%X")
print(t)

'''
from datetime import datetime
import pytz
local=datetime.now()
print("Local:",local.strftime("%m/%d/%Y, %H:%M:%S"))

tz_NY=pytz.timezone("America/New_york")
datetime_NY=datetime.now(tz_NY)
print("NY:", datetime_NY.strftime("%m/%d/%Y, %H:%M:%S"))

tz_London=pytz.timezone("Europe/London")
datetime_London=datetime.now(tz_London)
print("London:", datetime_London.strftime("%m/%d/%Y, %H:%M:%S"))'''

#Random :
#---------

#it is a built-in module of python which is used to generate the random numbers
#There are pseudo- random number algorithms used for generating the random number..

import random
print(random.random()) #it will display the floating random numbers between 0.0 to 1

print(random.randint(1,100))  #it will generate the positive random integer value

print(random.choice([10,3,5,68,20,13]))

li=[12,45,23,532,567,111,3,0]
random.shuffle(li)
print(li)


