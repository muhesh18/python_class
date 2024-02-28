#variable scope
#local variable

'''def sum(b):
    a=0
    a+= b
    return a
print(sum(70))

#global variable

def add(d):
    global a
    a=0
    a+=d
    return a
print(add(70))
print(a)'''

#nonlocal variable
def outer():
    c=0
    def inner1():
        nonlocal c
        c+=5
        print('inner1 is' , c)
    def inner2():
        nonlocal c
        c+=5
        print('inner2 is' , c)
    inner1()
    inner2()
outer()
#map
number =[1,2,3]
def lenn(a):
    return a*a

        
out=map(lenn, number)
print(list(out))
#map other method
c=[2,4,6,8]
out = map(lambda y:y*y ,c)
print(list(out))


#filter()
#filter(function,iterable)
a=[1,2,3,4,5,6,7,8,9,10]
even = filter(lambda y :( y%2==0),a)
print(list(even))

