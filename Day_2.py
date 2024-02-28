# Many Values to Multiple Variables
a,b,c=1,2,3
print(a,b,c)

# One Value to Multiple Variables
a=b=c=6
print(a,b,c)
print(a)

#Unpack a Collection
a=[1,3,57]
x,y,z=a
print(x,y,z)


# Python Strings
#  01234  - Forward Indexing

a="Aruvi"
#-5-4-3-2-1  - Backward Indexing

print("*"*50)
print(a)
# string [start:end:step]

print(a[:4])

print(a[0:4])

print(a[0:4:2])

print(a[0:4:3])


print(a[:4])

print(a[0:])

print(a[:])


print("*"*50)


print(a[-4:-1])

print(a[:-1])


print(a[::1])
print(a[::-1])
print(a[::-2])

'''
String Length
To get the length of a string, use the len() function.

'''
print("*"*50)
# len 

print(len(a))
a='python is'
print(len(a))

print("*"*50)

# Python - Modify Strings

a='  ARuvi     '
print(a)
print(a.upper())  # upper

print(a.lower())  # lower

print(a.strip())  # strip
print(a.lstrip())  # strip
print(a.rstrip())  # strip

print(a.replace('A','u'))  # replace

a='ARuvi, python     '
print(a.split(','))  # split


#  capitalize()	Converts the first character to upper case
a='aRuvi, python     '
print(a)
print(a.capitalize())


# casefold()	Converts string into lower case
a='aRuvi, python     '
print(a)
print(a.casefold())



# center()	Returns a centered string 
print("*"*90)

a='python'
print(a)
print(a.center(10))
print(a.center(10,"+"))

print("*"*90)


#count()	Returns the number of times a specified value occurs in a string


a='pppythonp.'
print(a.count('p',4,9))

# endswith()	Returns true if the string ends with the specified value

print(a.endswith('.'))

# find()Searches the string for a specified value and returns the position of where it was found


a='pppythonp.'
print(a.find('p',5))

print("*"*90)
# format()	Formats specified values in a string

name='python'
age =33
print(' is power fuill lanuage age is',name,age)

print(' {} is power fuill lanuage age is {}'.format(name,age))


print(' {1} is power fuill lanuage age is {0}'.format(name,age))


print(f' {name} is power fuill lanuage age is {age}')


name='Aravind'
age =25
print(f' age is {age} ,name is{name}')


# index

name='Aravind is A good boy '

print(name.index('A',5))




"""
Definition and Usage
The isalnum() method returns True if all the characters
are alphanumeric, meaning alphabet letter (a-z) and numbers (0-9)."""



A='@#$%'
print(A.isalnum())


"""
isalpha()	Returns True if all
characters in the string are in the alphabet


"""
a='adfagfrh678'
print(a.isalpha())


""""
Definition and Usage
The isdecimal() method returns True
if all the characters are decimals (0-9).

This method can also be used on unicode objects. See example below.


"""


