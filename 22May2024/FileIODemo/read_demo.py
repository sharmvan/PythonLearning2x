# f = open("vandana.txt", "r")
# print(f.read())
# f.close()
#
# f = open("vandana.txt", "r")
# print(f.readline())
# print(f.readline())
# print(f.readline())
# print(f.readline())
# f.close()
#
# f = open("vandana.txt", "r")
# print(f.readlines())
# f.close()

# read and write both:
f = open("vandana.txt", "r+")
print(f.readline())
f.close()

f = open("vandana.txt", "r+")
f.write("Some Content\n" "Some Content\n" "Some Content\n" "Some Content\n" "Some Content\n" "Some Content\n" "Some Content\n")
f.close()
