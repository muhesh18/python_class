#pattern
'''for i in range(5):
    print('*' * 5)'''

    

for i in range(6):
     print('*' * i)
for i in range(6):
    for i in range(i,5):
        print('*', end='')
    print()
for i in range(5,0,-1):
    print('*' * i)'''
    
'''n=int(input())
for i in range(n,0,-1):
    print((n-i) * ' ' + i *'*')'''
'''for i in range(5):
    for i in range(i+1):
        print('.',end="")
    for i in range(i,5):
        print('*', end="")
    print()'''

   
for i in range(5):
    for i in range(i+1):
        print('*', end=' ')
    print()
for i in range(5):
    for i in range(i,5):
        print('*' , end=' ')
    print()
    
        
