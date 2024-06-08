# get() - Returns the value for specified key in the dictionary.
# keys() - Returns a copy of dictionary's keys.
# items() - Returns a copy of dictionary's key value pair.
# values() - Returns a copy of values in the dictionary.
# pop() - Removes the item with the specified key.
# popitem() - Removes the arbitrary key:value pair.
# update() - Add the specified key:value pairs to dictionary.
# copy() - Returns a copy of dictionary
# clear() - Remove all the elements from the dictionary.

dic_1 = {1: 100, 2: 200, 3: 300, 4: 400, 'name': 'vandana', 'age': 100}
print(dic_1.get(1))
print(dic_1.keys())
print(dic_1.items())
print(dic_1.values())
print(dic_1.pop(4))
print(dic_1.popitem())

dic_1.update({"Home": "Asr"})
print(dic_1)

new_dic_1 = dic_1.copy()
print(new_dic_1)

new_dic_1.clear()
print(new_dic_1)
