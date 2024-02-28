#read csv file using file handling :(Comma Separated Values Source File (.csv))
#-------------------------------------

import csv                               #this is the module for csv
with open('olympics.csv','r') as file1:
    read=csv.reader(file1)               #this is the in-built function of csv module to read the file
    for i in read:
        print(i)
        break

print(dir(csv))
