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
