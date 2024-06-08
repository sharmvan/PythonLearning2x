# Manual steps to write to a file
# 1.Open notepad and create a file.
# 2.Write in the file.
# 3.Close the file
#
# Mode
# Read mode: r
# Write mode: w
# Append mode: a
# Read/Write: r+

f = open("vandana.txt", "w")
f.write("This is the 1st line.\n" "This is the 2nd line.\n" "This is the 3rd line.\n" "This is the 4th line.\n")
f.close()

# f = open("C:\\Users\\Sharmvan\\OneDrive - Landis+Gyr\\Desktop\\vandana.txt", "w")
# f.write("This is the 1st line")
# f.close()
#
# f = open("C:\\Users\\Sharmvan\\OneDrive - Landis+Gyr\\Desktop\\vandana1.txt", "w")
# l = [100, 200, 300, 400, 500]
# for i in l:
#     f.write(str(i) + "\n")
# f.close()
#
# f = open("C:\\Users\\Sharmvan\\OneDrive - Landis+Gyr\\Desktop\\vandana1.txt", "a")
# l = [100, 200, 300, 400, 500]
# for i in l:
#     f.write(str(i) + "\n")
# f.close()
