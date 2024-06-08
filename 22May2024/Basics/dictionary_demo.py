# Dictionaries are used to store data in key:value pairs.They are changeable and do not allow duplicate not values.

# Defining Dictionary
dic_1 = {}
dic_2 = {1: 100, 2: 200, 3: 300, 4: 400}
dic_3 = {'name': 'vandana', 'age': 100}
dic_4 = {'qa': 3, 3: 'url'}
print(dic_1)
print(dic_2)
print(dic_3)
print(dic_4)
print(type(dic_1))
print(type(dic_2))
print(type(dic_3))
print(type(dic_4))

# Accessing items from the dictionary
print(dic_2[1])
print(dic_3['name'])
print(dic_4['qa'])

# Adding items to dictionary
dic_4['prod'] = 'production'
dic_4[4] = 'SIT'
print(dic_4)

# Removing items from dictionary
dic_4.pop(4)
print(dic_4)
