"""WRITING TO FILES

1. USE THE 'w' mode
2. It will overwrite any files & file directory with same name

"""

with open("../Files/file2.txt","w") as File1:

    #Writing a message to a txt file
    #File1.write("This is line 1")
    #File1.write("This is line 2")

    #Using a list to write to a function
    Lines = ["Psalm 23 v 1 : The Lord is my shepherd I shall not want\n","Habbakkuk 2 v 2-3 : Then the Lord answered me and said ''Write the vision and Make it plain on the tablets, that he may run who reads it. For the vision is yet for an appointed time; But at the end it will speak and it will not lie. Though it tarries, wait for it; Because it will surely come, it will not tarry.\n"]

    #Use a for loop to iterate their entrances into the file
    for line in Lines:
        File1.write(line)

        print(line)

"""APPENDING TO FILES

1. USE THE 'a' mode
2. It will overwrite any files & file directory with same name

"""

with open("../Files/file2.txt","a") as File2:

    new_line = "Psalm 27 v 1 : The Lord is my light and my salvation, whom shall I fear? The Lord is the strength of my life, of whom shall I be afraid?\n"

    File2.write(new_line)

"""COPYING FILES FROM 1 FILE TO ANOTHER

1. USE THE 'r' mode to GET THE INFO
2. USE THE 'w' mode to WRITE THE INFO INTO NEW FILE

"""

#THis is the source file
with open("../Files/file2.txt",'r') as File3:

    #This is the destination file
    with open('../Files/file1.txt','w') as File4:
        #Read the lines from the SOurce file and then use the forloop to write them into the Destination file
        for line in File3:
            File4.write(line)


"""MODES

‘r’ 	'r' 	Read mode. Opens an existing file for reading. Raises an error if the file doesn't exist.
‘w’ 	'w' 	Write mode. Creates a new file for writing. Overwrites the file if it already exists.
‘a’ 	'a' 	Append mode. Opens a file for appending data. Creates the file if it doesn't exist.
‘x’ 	'x' 	Exclusive creation mode. Creates a new file for writing but raises an error if the file already exists.
‘rb’ 	'rb' 	Read binary mode. Opens an existing binary file for reading.
‘wb’ 	'wb' 	Write binary mode. Creates a new binary file for writing.
‘ab’ 	'ab' 	Append binary mode. Opens a binary file for appending data.
‘xb’ 	'xb' 	Exclusive binary creation mode. Creates a new binary file for writing but raises an error if it already exists.
‘rt’ 	'rt' 	Read text mode. Opens an existing text file for reading. (Default for text files)
‘wt’ 	'wt' 	Write text mode. Creates a new text file for writing. (Default for text files)
‘at’ 	'at' 	Append text mode. Opens a text file for appending data. (Default for text files)
‘xt’ 	'xt' 	Exclusive text creation mode. Creates a new text file for writing but raises an error if it already exists.
‘r+’ 	'r+' 	Read and write mode. Opens an existing file for both reading and writing.
‘w+’ 	'w+' 	Write and read mode. Creates a new file for reading and writing. Overwrites the file if it already exists.
‘a+’ 	'a+' 	Append and read mode. Opens a file for both appending and reading. Creates the file if it doesn't exist.
‘x+’ 	'x+' 	Exclusive creation and read/write mode. Creates a new file for reading and writing but raises an error if it already exists.


"""
