# Pass: is used to skip the code
for i in range(10):
    if i == 5:
        pass        # If we are using pass, else condition will be executed.
    else:
        print(i)
print("---")

for i in range(10):
    if i == 5:
        break
    else:            # But in case of break, After break else wouldn't be interested
        print(i)
print("---")

for i in range(10):
    if i == 5:
        pass
else:
    print(i)


