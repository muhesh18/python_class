#with the usage of with function we don't need to close the file
#it will automatically close the file once we open
'''
with open('File11 txt file.txt','r') as file1:            #file1 is a variable name
    print(file1.read())

with open('with in File Handling.txt','r') as file1:            #file1 is a variable name
    #str(file1).upper()
    #print(str(file1).upper())
    print(file1.read().upper())                                 #it will read and give the output is upper
    #print(file1.upper().read())

print("-"*50)   #or

with open('with in File Handling 1.txt','x+') as file1:
    file1.write("hi i am learn python\npytnon language is very\npowerful\ni learn easy")
    file1.seek(0)
    print(file1.read().upper())
'''

#ONE TEXT FILE TO COPY TO ANOTHER TEXT FILE :
#----------------------------------------------

with open('with in File Handling 1.txt','r') as file,\
     open('with in File Handling 2.txt','x+') as file1:
    for i in file:
        file1.write(i)
    file1.seek(0)            #in this the cursor is in last once we write...so we use seek to set the cursor in the top...
    print(file1.read())
