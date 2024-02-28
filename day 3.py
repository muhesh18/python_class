#List
#List is a collection of element
#Lists are used to multiple items in a single variable
#list is mutable datatype
#list items are ordered,changeble and allow duplicate values.
#list are created using square brackets [].

#type
a =[]
print(type(a))
'''#length
b= ['banana' , 12, 13.4]
print(len(b))

#Accesing items in the list
b= ['banana' , 12, 13.4]
print(b[1])

#Negative indexing
b= ['banana' , 12, 13.4,'orange','apple','jackfruit',123]
print(b[-4:-1])

#Range of index

b= ['banana' , 12, 13.4,'orange','apple','jackfruit',123]
print(b[2:5]) 

b= ['banana' , 12, 13.4,'orange','apple','jackfruit',123]
print(b[2:]) 

#change List items
#Tochange the value of specific item

b= ['banana' , 12, 13.4,'orange','apple','jackfruit',123]
b[1] = 'Name'
print(b)'''

#change the range of item values
'''
b= ['banana' , 12, 13.4,'orange','apple','jackfruit',123]
print(b)
b[2:6] =['name',14.5,'light','white']
print(b)

#Insert Items
#To insert a newlist item without replacingany of the existing values we use insert()
b= ['banana' , 12, 13.4,'orange','apple','jackfruit',123]
b.insert(3,2.4)
print(b)'''

'''#append items
b= ['banana' , 12, 13.4,'orange','apple','jackfruit',123]
b.append("jack")
print(b)
#extend list
thelist =["add", "subtract", "minus"]
fruit = ["grapes", "apple", "banana"]
thelist.extend(fruit)
print(thelist)'''
a=[[1,2,3],[4,5,6]]
b=a[0]
c=a[1]
b.extend(c)
for i in range(6):
    print(b[i])

#Add any iterable
#the extend() method does not have to append list you can add any iterable objects

'''a=[1,70,True,"Hello"]
print(a)
print(type(a))

a=[0,1,7,8,9,10]
a[1] =8
print(a)

a=[1,2,3,4]
print(len(a))
'''
'''print(a[3])
print(a[-1])
print(a[2:4])
print(a[1:3])
print(a[-4:-1])
print(a[::])
print(a[::-1])
print(a[::-2])'''

#change list item
'''age =[27,87,100,101,72]
print(age)
age[2:4] = [41,42]
print(age)
age[-4:-2] =0,1
print(age)
cat =['Big', 'small', 'large']
cat.append('Big large')
print(cat)
cat.insert(2,'Big Large')
print(cat)
dog=['verysmall', 'small']
cat.extend(dog)
print(cat)
#remove list item
a=[1,2,3,4,5]
a.pop()
print(a) #pop remove the last value
a.pop(0) #remove first value access index
print(a)'''

