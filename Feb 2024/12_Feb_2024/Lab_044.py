# Break: This is used for kicking out from the loop.
# for -> 1 to 10 -> range (1,11,1) , range(1,11)
# i=5 -> break from the loop - Kicked out from the loop.
for i in range(1, 11):
    if i == 5:
        break
    print(i)
print("out of the loop")
print("----")

for i in range(1, 11):
    print(i)
    if i == 5:
        break
print("out of the loop")

