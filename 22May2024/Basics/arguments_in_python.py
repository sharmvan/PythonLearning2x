# Positional Arguments
# Keyword Arguments
# Required Arguments
# Optional Arguments
def sub(x=40, y=50):  # when we define a functions with sum values that is called "parameters". Here x and y are "parameters".
    return x - y


print(sub())  # But while calling the functions when we provide the actual values this becomes "arguments".
print(sub(30, 20))
print(sub(30))
print(sub(y=20))
