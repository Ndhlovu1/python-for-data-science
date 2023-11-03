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