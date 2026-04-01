
# FILE HANDLING
#=================


# save the data to another file (write)
# read from another file
# modify the exisiting file


# modes (used to know ur intention when we open the file in python module)
#============================================================================

# read   "r"
# write  "w"
# append "a"

# read >> "r"  file should be existing else error will be raised
# write >> "w" write the file from scratch (erase if there is any existing data)
#              if file doesnt exist , create a new file then start writing

# append >> "a"  write at the end of the existing data (file)


# open()

# close()

# example

# read

# file = open("file.txt","r")

# result = file.read()       # used to read the entire content from first to last

# print(result)

# file.close()

# write

# file = open("file.txt","w")

# file.write("Thankyou guysssss")           # erase the existing content and write this to the file

# file.close()

# append

# file = open("file.txt","a")

# file.write(" For your valuable time")           # append the content with the existing content , here we use the write method .

# file.close()

# with open("file.txt","r") as file:      # The file is automatically closed after the 'with' block

#     content = file.read()           

#     print(content)

