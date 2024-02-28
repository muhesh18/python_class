#check string
a='python is most powerful'
print('the' in a)
print('the' not in a)

#string slicing
'''a='Hi Hello Good'
print(a[0])
print(a[1:4])
print(a[6:12])
print(a[-5:])
print(a[-7:-1])
print(a[-12:])'''
b="Python is more powerful"
'''print(b[::])
print(b[::1])
print(b[::2])'''
#reverse the string
print(b[::-1])
print(b[2:10:2])
#string concatenation
a="Python"
b="Good"
print(a+b)
#string format
name = 'Aruvi'
age =22
print('name is, Age is' ,name,age)
print('name is {}, Age is {}'.format(name,age))
print(f'name is {name}, age is {age}')

name ='Aruvi'
age =10
salary =1100000
print(f'name is {name} ,age is {age}, salary is {salary}')
#string modify
a='PYTHON'
print(a.lower())
c='PYTHON'
print(c.swapcase())
a= 'python'
print(a.capitalize()) #first letter will be capital
d='python'
print(d.center(20, '*'))
a='python python'
print(a.count('p'))
d="pytho is a most is"
print(d.count('is'))
print(d.endswith('is'))
print(a.find('o',5))
