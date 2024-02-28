#recursion
'''num = 5
def fact(a):
    if a==1:
        return 1
    else:
        return(a*fact(a-1))
print(fact(num))
'''

a=0
b=1
for i in range(15):
    c=a+b
    a=b
    b=c
    print(c)

a=0
b=1
def fibo(a,b):
    if a<=5 and b<=5:
        return
