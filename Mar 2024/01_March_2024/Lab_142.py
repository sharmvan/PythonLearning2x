# Another way which people recommended:
# How to handle "FileNotFoundError"?
# "with" keyword means with opening the file, get the content.
# instead of writing this-> file = open("TestData1.txt", 'r'), we can use: with open("TestData.txt", "r") as file:
try:
    with open("TestData.txt", "r") as file:
        content = file.read()
        print(content)
except FileNotFoundError as fnfe:  # fnfe: file not found error
    print(fnfe)
finally:
    file.close()
# Advantage of "with" keyword means we can wrap our code.
