'''num =1
even = filter(lambda i:(i%2==0), range(num,100))
print(list(even))
num =2
even_2 =filter(lambda x:x if x%2==0 else'' ,list(range(1,101)))
print(list(even_2))
'''
#lambda arguments:expression
'''square =lambda x:x*x
print(square(10))'''
#map
#syntax
'''map(function, iterable)
iterable = list,set,tuple,dict
a=['apple', 'banana' ,'cherry']
print(list(map(len,a)))'''
a=[10]
b=[30]
out =map(lambda x,y :(x+y),a,b)
print(list(out))
