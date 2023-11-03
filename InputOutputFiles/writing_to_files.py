"""WRITING TO FILES

1. USE THE 'w' mode
2. It will overwrite any files & file directory with same name

"""

with open("../Files/file2.txt","w") as File1:

    #Writing a message to a txt file
    File1.write("This is line 1")

