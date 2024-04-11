# File Handling: means How to Read a text, and write into this file using python code.
# Suppose I have simple file i.e. "TestData.txt" and how Can I read this file?
# Before reading a file, we need to check below first:
# function-> which function should we use to read a file?
# Mode-> what is the mode it has? There are many types of modes which are supported by python.

# flow for a file handling:-
# To read a file, we have inbuilt function i.e. open ("file_name","mode")

# Mode-
# 'r' for reading (default)--> you want to read the file only. you don't want to write.
# 'w' for writing (creates a new file or truncates an existing one)
# 'a' for appending
# 'b' for binary mode--> used for .exe files like vlc.exe. vlc is used for song playing (media player) for eg: zoom.exe.
# '+' for updating (reading and writing)

# we can Read and Write content
# Read a file
# Reading Entire Content: Content = file_object.read()
# line = file_object.readline() for a single line.
# lines = file_object.readlines() for all lines in a list.

# In the end, we have to close the file.

file = open("TestData1.txt", 'r')  # If I mention wrong file name I will get an error FileNotFoundError: [Error 2] No
# such file or directory: 'TestData1.txt'
# How to handle it, refer Lab_142

# file = open("TestData.txt", 'r')  # Give name of the file and in which mode you want to open
content = file.read()  # Read the content of the file
print(content)  # Print the content
file.close()  # And close the file

# Another way which people recommended: "with" keyword, refer Lab_142
