a = "building"
i = 0
while i < len(a):
    print(i)  # If you use i, it will start from 0 and will give the values like 0,1,2,3,---
    print(a[i])  # If you want to access a particular character then you will use a[i]. we want value of a[i]
    i = i + 1

print("-----")

a = "building"  # --> the moment you use string, it is converted into list [b,u,i,l,d,i,n,g]
for i in a:  # each character we can access by i.
    print(i)
