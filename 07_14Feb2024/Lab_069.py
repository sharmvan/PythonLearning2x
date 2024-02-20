# Problem statement: try to resolve this below program
name = input('enter a name\n')  # naman
length = len(name)  # 5
reverse = ""
for i in range(length - 1, -1, -1):
    reverse = reverse+name[i]
    print(reverse)
