# How to write in csv file?
import csv

# Suppose I have below data and I want to write this test_data into csv file.
test_data = [
    ['Name', 'Age', 'City'],
    ['Vandana', '100', 'London'],
    ['Kajal', '65', 'New York']
]
# with open("mydata.csv", 'w') as file:
#     writer = csv.writer(file)
#     for data in test_data:
#         writer.writerow(test_data)

# above code, we can handle with try and except as well.
try:
    with open("mydata.csv", 'w') as file:
        writer = csv.writer(file)
        for data in test_data:  # test data we want to write in "mydata.csv" file
            writer.writerow(test_data)  # with writerow method means every row will pick from test data, and we will keep writing.
except FileNotFoundError as f:
    print(f)
finally:
    print("Close your files!!")
    # close the file code.
