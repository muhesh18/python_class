
'''def add(a,b):
    return a**b
print(add(101,11))


def squares(a):
    for x in a:
        print(x**2, end=' ')

squares([1,6,11,100,7])






def names(a):
     for x in a:
        if x=='cherry':
            print(x)

names(['apple' ,'cherry', 'orange', 'Gova'])'''

#keyword arguments
'''def add(a,b):
    return a+b
print(add(a=5,b=6))

def add(a=5,b=6):
    return a+b
print(add())

#Arguments with default values
def add(a, b=6):
    return a+b
print(add(6,1))
def add(a, b=6):
    return a+b
print(add(6))'''

'''def add(b,a=8):
    return a+b
print(add(6))'''

'''a=[1,2,3,4,5]
def adding(a):
    c=0
    for x in a:
        c=c+x
    print(c)
adding([1,2,3,4,5])'''

def number(num):
    if(num%2)==0:
        print("{0} is even" .format(num))
    else:
        print( "{0} is odd".format(num))
number(int(input()))
































































































