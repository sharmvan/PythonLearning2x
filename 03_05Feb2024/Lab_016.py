name='Vandana Sharma'
print(len(name))#--len always starts from 1--For len() round brackets, for indexes [] square brackets
print(name[0])
print(name[8])
#print(name[20])#IndexError: string index out of range

print(len(name)-1)
print(name[len(name)-1])

# String immutability- that can't be changes'. once we created then we can't modify.
string='Vandana'
string[5]='n'#TypeError: 'str' object does not support item assignment but we can replace the value like below
string='Anisha'

