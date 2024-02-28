'''
file=open('create a new txt file.txt','x')         #x means create a new txt file name as 'create a new txt file'
file.write('yehya is my friend son he is a good')
file.close()

file=open('create a new txt file 1.txt','x')
file.write('1 2 3 4 5 \n6 7 8 9 10 \n11 12 13 14 15 \n16 17 18 19 20')
file.close()

file=open('create a new txt file 2.txt','w')
for i in range(1,21):
        file.write(str(i)+' ')
        if i%5==0:
            file.write('\n')
file.close()'''


file=open('create a new txt file 3.txt','w+')
for i in range(1,21):
        file.write(str(i)+' ')
        if i%5==0:
            file.write('\n')
file.seek(0)
a=file.readline()
b=file.readline()
c=file.readline()
d=file.readline()
print(sum([int(i) for i in a.split()]))
print(sum([int(i) for i in b.split()]))
print(sum([int(i) for i in c.split()]))
print(sum([int(i) for i in d.split()]))
file.close()

print('-'*60)
file1=open("create a new txt file 3.txt",'r')
for i in file1:      #it will read the line without using read function
        print(i)   
file1.close()

print('-'*60)
file1=open("create a new txt file 3.txt",'r')
for i in file1:      #it will read the line without using read function or readline
        print(i)   
        break
file1.close()
