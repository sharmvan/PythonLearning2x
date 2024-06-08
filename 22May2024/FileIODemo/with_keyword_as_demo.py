# fw = open("demofile.txt", "w")
# fw.write("Vandana is my name.")
# fw.close()
#
# fr = open("demofile.txt", "r")
# print(fr.read())
# fr.close()

# instead of above, I can use 'with' keyword.
with open("demofile.txt", "w") as fw:
    fw.write("I'm going to write some content here in this file")

with open("demofile.txt", "r") as fr:
    print(fr.read())