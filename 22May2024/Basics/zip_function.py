list_1 = ['Apple', 'Banana', 'Mango', 'Orange', 'Grapes']
list_2 = ['Asr', 'Banaras', 'Meghalya', 'Orissa', 'Gujarat']
s = zip(list_1, list_2)
print(s)

print("---------------------------------------------------------------")

print(list(s))

print("---------------------------------------------------------------")

for i, j in zip(list_1, list_2):
    print(i, j)

print("---------------------------------------------------------------")

total_price = [500, 200, 100]
sale_price = [150, 100, 50]
for t,s in zip(total_price,sale_price):
    print(t-s)

print("---------------------------------------------------------------")
