# How to print all the lines?
with open("td.txt", 'r') as file:  # "td.txt" is in read format
    lines = file.readlines()  # If I want to print all the lines then use: readlines() function
# print(lines) # This is coming in list format
for line in lines:
    print(line,end="")

# How to append in an existing file? append means, we keep writing in the end.
with open("td.txt", 'a') as file:
    file.write("Anmol")