'''file1 = open("25file.txt", "r")
for i in file1:
    print(i)
    #break

file1.close()

#with
with open("25file.txt", 'r') as file1:
    print(file1.read())
#task

hi i am learn python
python language is very
powerful
i learn easy

with open("25file.txt", 'r') as file1:
    print(file1.read().upper())

with open("305file.txt" , "x+" ) as file1:
    file1.write("Hi i am learn  python \n python language")
    file1.seek(0)
    print(file1.read().upper())

#one file to copy another file
with open('file9.txt' , 'r' ) as file, open('file110.txt' ,'a+') as file_23:
    for i in file:
        file_23.write(i)
    file_23.seek(0)
    print(file_23.read())
#read csv file using file handling
'''
import csv
with open('olympics.csv', encoding='utf-8',errors='replace') as file1:
    ree=csv.reader(file1)
    for i in ree:
        print(i)

#with open('your_file.txt', 'r', encoding='utf-8', errors='replace') as file:
#
content = file.read()
#try except
a=5
b=0
try:
    print(a+b)
except: 
    print('your input is wrong')
#try except
a=5
b='7'
try:
    with open('25file.txt', 'r') as file:
        print(file)
except:
    print('your file is not created')

try:
#some code
except:
#executed if error in the
#try block
else:
#execute if no exception
finally:
#some code... (always executed)
