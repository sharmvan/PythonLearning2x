# max() Returns the largest item in an iterable
# min() Returns the smallest item in an iterable
# iter() Returns an iterator object
# reversed() Returns a reversed iterator
# next() Returns the next item in an iterable
# slice() Returns a slice object
# sorted() Returns a sorted list
# sum() Sums the items of an iterator
# input() Allows user to input value
list_demo = [100, 500, 200, 300, 500]
print(max(list_demo))
print(min(list_demo))

print(iter(list_demo))  # <list_iterator object at 0x000001D9B8033C10>

i = iter(list_demo)
print(list(i))  # [100, 500, 200, 300, 500]

i = iter(list_demo)
print(next(i))
print(next(i))
print(next(i))
print(next(i))
print(next(i))

j = reversed(list_demo)
print(next(j))
print(next(j))
print(next(j))
print(next(j))
print(next(j))

s = slice(1, 5, 2)
print(list_demo[s])

so = sorted(list_demo)
print(so)

sum_1 = sum(list_demo)
print(sum_1)  # It will print sum of all the items i.e. 1600

sum_1 = sum(list_demo, 100)
print(
    sum_1)  # it will print sum of all the items i.e. 1600 and will add 100 (Start value) . Hence, result will be 1700.

x = input("enter your name: ")
print(f"Weocome {x}")
