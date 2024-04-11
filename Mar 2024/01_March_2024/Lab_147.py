# Suppose I have data present in data.csv file
# How to read CSV file? CSV nothing but comma separated value, kind of Excel file.
import csv  # Python has inbuilt csv module.

with open("data.csv") as csvfile:  # directly we can ready without mentioning "r" mode if we want to read.
    reader = csv.reader(csvfile) # reader will give you all the data.
    for col in reader:
        print(col[0], col[1], sep="|")
