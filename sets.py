#sets
'''
a={1,2,3,4}
print(a)
print(type(a))
name ={'Apple','Boy', 'Good'}
print(name)
#not allow duplicates
name ={'Apple' ,'Boy', 'Good', 'Boy', 'Good'}
print(name)
#unindex
print(name[0])
#unchangeable
print(name[0] ='0')
name={'Apple', 'Boy' ,'Good', 'Boy', 'Good'}
#name.add('0')
#print(name)
#update used to store multiple values

name.update((7,8,9))
print(name)
#remove
a={7,8,10,8,11}
#a.remove(12)
print(a)
#a.discard(8)
print(a)
a.pop()
print(a)
a={7,8,10,100,200}
a.clear()
print(a)'''
a={1,2,3,4}
b={7,8,9,10,1,2}
#print(a.union(b))
#print(a.intersection(b))
print(a.difference(b))
print(a.symmetric_difference(b))
#subset displays true or false
a= {1,2,3,4}
b={1,2}
#print(b.issubset(a))
print(b.issubset(a))
print(b.issuperset(a))
