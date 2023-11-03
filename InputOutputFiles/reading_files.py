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

1. USING A WITH STATEMENT AUTO CLOSES 

"""

with open("../Files/file1.txt","r") as File2:
    print("\n----------------read()----------------------")

    #Start reading the files
    file_info = File2.read()
    print("----------------------------------")
    print("READING FILE INFORMATION")
    print(file_info)
    print("END OF FILE INFORMATION")
    print("----------------------------------")


print("FILE CLOSED : ",File2.closed)
print("--------------------------------------")


"""PASSING THE FILE INTO A LIST BASED ON LINES 

1. USING THE readlines() automatically assigns the file as a list with each new line seen as a new index position
2. It adds the \n into the mix to show a new line

"""

with open("../Files/file1.txt","r") as File3:
    print("\n----------------readlines()----------------------")

    single_line_info = File3.readlines()

    print(single_line_info)


"""READING ONLY THE VERY FIRST LINE

1. Printing a single line at a time
2. Auto iteration

"""

with open("../Files/file1.txt","r") as File4:

    print("----------------readline()----------------------")

    single_line_info = File4.readline()

    print("LINE 1 :",single_line_info)

    single_line_info = File4.readline()

    print("LINE 2 :",single_line_info)


