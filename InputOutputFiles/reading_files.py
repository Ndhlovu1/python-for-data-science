# READING FILES IN PYTHON 

"""SYNTAX
1. Use the open()
2. Pass the Mode 
    1. r = Reading
    2. w = Writing
    3. a = Appending

"""

File1 = open("../Files/file1.txt","r")

#Obtain the name of the file by printing the object name
nm = File1.name
print(nm)

#Get the mode being used
md = File1.mode
print(md)

#Close the Project
File1.close()

"""ALTERNATIVE

"""

