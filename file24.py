'''file = open('file5.txt' , 'x')
file.write('good morning')
file.close()

#task
#new file create store values
1 2 3 4 5
6 7 8 9 10
file = open('file6.txt','w')
for i in range(1, 21):
    file.write(str(i) + " ")
    if i%5 ==0:
        file.write('\n')
file.close()'''

file = open('file6.txt','w+')
for i in range(1, 21):
    file.write(str(i) + " ")
    if i%5 ==0:
        file.write('\n')
file.seek(0)
a= file.readline()
b= file.readline()
c= file.readline()
d= file.readline()
print(a)
print(sum([int(i) for i in a.split()]))
print(sum([int(i) for i in b.split()]))
print(sum([int(i) for i in c.split()]))
print(sum([int(i) for i in d.split()]))
file.close()

#task
#no.of student -first input
#how many subject - second input
#example
'''
22 44 66 77 88 - st1
44 77 22 11 77 - st2
66 55 44 33 77 -st3''' a
file = open('file6.txt', 'w+')
no_of_student = int(input())
how_many_subject = input()

