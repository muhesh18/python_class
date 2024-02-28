#frozen set
#unorder
#unindex
#not allow duplicate

#Not allow duplicate
'''a=frozenset((1,2,3,4,1,2,3))
print(a)
print(type(a))

#unorder
b=frozenset(('aravind' ,'krishna' ,'Mathan'))
print(b)
print(dir(b))'''

a=[1,2,3]
b=a
b[0] =10
print(a,b)

a=[1,2,3]
b=a.copy()
b[0] =10
print(a,b)

a=[1,8,10,2,4]
a.sort()
print(a)
a.reverse()
print(a)

#dict
a={'a' :1, 'a':2}

a.update({'b' :3})
print(a)
a['c']=4
print(a)
a.get('a')
print(a)

#Tuple

