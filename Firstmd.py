'''def greeting(name):
    print("Hello, " + name)
def add(a,b):
    print(a+b)
def sub(a,b):
    print(a-b)
def mult(c,d):
    print(c*d)
def divi(e,f):
    print(e/f)
def modu(g,h):
    print(g%h)'''
#three input
#first give username
#second give password
#three give repassword
#the suiccess show your success login
name="Aravind"
first_name = input("Enter your first_name:")



if name==first_name:
    second =input("Enter your second password:")
    repassword =input("Enter your repassword:")
    if second ==repassword :
        print("login succesful")
else:
    print("login unsuccesful")
        

