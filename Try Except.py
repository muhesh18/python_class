#Try Except

'''
try:
    #Some Code
except:
    #Executed if error in the
    #try block
else:
    #execute if no exception
finally:
    #some code...(always executed)
'''

a=5
b=0
try:
    print(a/b)
except:
    print("The Input is Wrong")

a=5
b='0'
try:
    print(a+b)
except:
    print("This Process is False...")

a=5
b='7'
try:
    with open("python.txt",'r')as file:
        print(file)
except:
    print("your file is not create...")


print('-'*50)
def divide(x,y):
    try:
        result=x//y
        print(result)
    except ZeroDivisionError:
        print("Sorry! You are dividing by Zero")
    else:
        print("hi")
divide(3,2)
divide(3,0)

print("-"*50)
try:
    #Code that might raise an exception
    result=10+'0' #This will raise ZeroDivisionError
except ZeroDivisionError:
    #if we type two errors we can type the type of error in except
    #Handle specific exception
    print("Error : Division by zero")
except Exception as e:   #it will show up the type of error we don't know..
    #Handle any other exceptions
    print("An error occurred:",e)
else: 
    #This block executes if no exceptions occur
    print("Division successful.Result:",result)
finally: #This will run Anytime and this is the end of the code
    #This block always executes,regardless of exceptions
    print("Cleanup or final tasks here")

print("-"*50)
try:
    file=open('file1.txt','r')
    print(file.read())
except Exception as jesi:
    print("An Error Occured :",jesi)

print("-"*50)
try:
    file=open("File Handling in Python txt file.txt",'r')
    print(file.write("HI"))
except Exception as e:
    print("An Error Occured :",e)
finally:
    print("Have a good day")


#-------------------------------------------------------------------------  
print("-"*50)
def read_file(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
            print("File contents:")
            print(content)
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    except PermissionError:
        print(f"Error: Permission denied to access '{filename}'.")
    except IOError:
        print(f"Error: Input/Output error occurred while reading '{filename}'.")
    except Exception as e:
        print(f"Error: An unexpected error occurred: {e}")

def write_to_file(filename, content):
    try:
        with open(filename, 'w') as file:
            file.write(content)
            print(f"Content successfully written to '{filename}'.")
    except PermissionError:
        print(f"Error: Permission denied to write to '{filename}'.")
    except IOError:
        print(f"Error: Input/Output error occurred while writing to '{filename}'.")
    except Exception as e:
        print(f"Error: An unexpected error occurred: {e}")

def append_to_file(filename, content):
    try:
        with open(filename, 'a') as file:
            file.write(content)
            print(f"Content successfully appended to '{filename}'.")
    except PermissionError:
        print(f"Error: Permission denied to append to '{filename}'.")
    except IOError:
        print(f"Error: Input/Output error occurred while appending to '{filename}'.")
    except Exception as e:
        print(f"Error: An unexpected error occurred: {e}")

def main():
    try:
        filename = input("Enter filename: ")
        read_file(filename)

        content_to_write = input("Enter content to write to the file: ")
        write_to_file(filename, content_to_write)

        content_to_append = input("Enter content to append to the file: ")
        append_to_file(filename, content_to_append)
    except KeyboardInterrupt:
        print("\nProgram terminated by user.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if _name_ == "_main_":
    main()
