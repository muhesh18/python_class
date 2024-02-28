#There are three modes in file handling :
#-----------------------------------------

#1.read(r)-this is the default mode,which opens a file for reading.
#2.write(w)-this mode opens a file for writing.if the file does not exist,it creats a new file.
#3.append(a)-opens a file in append mode,so that you can append data to end of file.if the file does not exist,it creates a new file.
#(b)-means opens a file in binary mode.
#'r+' - opens a file for reading and writing.
#'w+' - opens or creates a file for writing and reading,discards existing contents.
#'a+' - opens or creates a file for reading and writing.and appends data to the end of file.


file1=open("File Handling in Python.txt",'r')   #file1 is a variable name... 'r' means read...
print(file1.read())
file1.close()
print('-'*50)

new=open('D:/PYTHON COURSE/File Handling in Python txt file.txt','r')   #for different file location files we can access by using the location
print(new)                                #it will give the memory address of the file
print('-'*50)
print(new.name)                            #it will give the name of the txt file...
print(new.mode)                            #it will give the mode we use read or write....
print('-'*50)
print(new.readline())                       #it will give the first line of the txt file...
new.seek(0)                                 #seek means it will move the cursor based on the index value...
print('-'*50)
print(new.read())                          #it will give the full output present in the txt file...
new.seek(0)
print('-'*50)
print(new.read(10))                         #it will give the output based on the index value
new.seek(0)
print('-'*50)
print(new.readlines())                      #it will give the output in list format...
new.seek(0)
print('-'*50)
new.close()
print('-'*50)


file1=open("File Handling in Python.txt",'w')   #file1 is a variable name... 'w' means write...
file1.write('Welcome to my Youtube Channel..........')
file1.close()
print('-'*50)


file1=open("File Handling in Python.txt",'a')   #file1 is a variable name... 'a' means append...
file1.write('Hello my name is mathavan.....')
file1.close()
print('-'*50)

