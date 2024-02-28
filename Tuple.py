#Tuple
#ordered
a=(1,2,3,4)
print(a)
print(type(a))
b=('banana' ,'apple','dragonfruit')
print(b)

#unchangeable
'''b[1] ='strawberry'
print(b)'''

#allow duplicates
a=(1,2,3,4,4)
print(a)

#start index is 0
a=(1,2,3,4)
print(a[0])
a=(1,2,3,10,101)
print(a[-3:-1])
print(a[:4])
print(a[0:4])
print(a[-1::-1])
print(a[::1])
print(a[::-1])
print(a[-4:])
print(a[-4:-1:2])
print(a[-1:-4:]) 
print(a[-1:])
print(dir(tuple()))
#count
a=(7,8,9,10,2,4,9,8,9,8)
print(a.count(9))
#index
a=(7,8,9,10,2,4,9,8,9,8)
print(a.index(10))
print(a.index(9,3))
print(a.index(9,2))
b=(1,1,1,2,2,3,3,4,1)
print(a.index(2,0,4))
#we cannot change the tuples if we want to change we can change it into list and we can make tuple

