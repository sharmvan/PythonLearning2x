# Write a program that calculates and displays the letter grade for a
# given numerical score (e.g., A, B, C, D, or F) based on the following grading scale:
# input- score - 89
# output- B
# A: 90-100
# B: 80-89
# C: 70-79
# D: 60-69
# F: 0-59
# Use If, elif, else
# For every problem statement, we have to do 3 steps.
# Step 1: Figure out the inputs, What will be the inputs that user will give us? --int numbers (numerical scores)
# score I will be chacking what is the grade in this case?
score = int(input("Enter score: "))
# Step 2: Figure it out logic. Logic says that I have to print A-> If score >= 90 and score <= 100 and so on
# according to conditions & Step 3: Print output
if (score >= 90) and (score <= 100):
    print("Grade A")
elif (score >= 80) and (score <= 89):
    print("Grade B")
elif (score >= 70) and (score <= 79):
    print("Grade C")
elif (score >= 60) and (score <= 69):
    print("Grade D")
elif (score == 60) and (score <= 59):
    print("Fail")
else:
    print("Invalid Grade")
