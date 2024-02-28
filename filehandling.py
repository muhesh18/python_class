'''file1 = open("firstfile.txt" , 'r')
print(file1.read())
file2 = open("fileha.txt" , 'r')
print(file2.read())
file2.close()
print(file2.read())'''

file_3 =open("fileha.txt" , 'w+')
file_3.write("Name")
file_3.seek(0)
print(file_3.read())
