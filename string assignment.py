#String Manipulation
#print the length of the string
'''A='Kumar'
print(len(A))
#String in uppercase
A = 'Krishna'
B= A.upper()
print(B)
#String in lowercase
A='KRISHNA'
B=A.lower()
print(B) 
#String first and last characters
A= 'KRISHNA'
B = A[0]
C= A[6]
print(B)
print(C)'''

lis=[1, 90, 56, 90, 90, 50,30,2]
#print(lis.index(90,5))
#print(lis[-4:-2])
#d={'Name':"Bala" ,'ID' :908353, 'Age' :22, 'Degree':'BSC'}
value ={}
#print(value)
#print(type(value))
value['Num'] ='100'
#print(value)
#Replacing  dictionary elements
value['Num'] = '250'
#print(value)
#Adding multiple elements to the dictionary
value.update({'Fruits':'orange', 'color':'Red'})
#print(value)
print(value.keys())
print(value.values())
print(value.items())
#Accesing the dictionary element
print('Fruits is :', value['Fruits'])
print('color is: ', value.get('color'))
print('Num is :' , value.get('Num'))
#to find the length of the string
print(len(value))
A={20:40, 'Aruvi':'siva', 'age':22}
print(A.keys())
print(A['Aruvi'])
#deleting the dictionary
del A['Aruvi']
print(A)
A .pop('age')
print(A)
#copy
a= {20:40,"Aruvi" : "Siva", "age":22}
b= a.copy()
print(b)
#from keys
a=[20,30,40,50,60]
b=dict.fromkeys(a)
print(b)
a={20:40 ,50:60}
a.update(
