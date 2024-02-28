#Many values to multiple variables
'''a,b,c = 1,2,3
print(a,b,c)

a=b=c=6
print(a,b,c)

a=[1,3,27]
x,y,z=a
print(x,y,z)'''

a="Aruvi"
print(a[:4])

print(a[0:4])
print(a[0:4:2])
print(a[0:4:3])
print(a[:4])
print(a[-5:-1])

'''a=0
while a<=5:
    print(a)
    a+=1'''


'''a=22
while a<=57:
    print(a)
    a+=1'''
'''a=0
while a<=10:
    print(a)
    if a==5:
        break
    a+=1'''

'''a=0
while 0<=10:
    a+=1
    if 5<1<10:
        continue
    print(a)'''
'''    
a=-1
while a<50:
    a+=1
    if a%2!=0:
        continue
    print(a)'''
    
a=int(input())
if a==0:
    print("It is not number")
elif a>0:
    while a<50:
        a+=1
        if a%2==0:
            continue
        print(a)
