# Reverse a string. for eg: vandana -> anadnav
# original_str = input("Enter any name\n")
# reverse_str = ""
# for c in original_str:
#     reverse_str = c + reverse_str
# print(reverse_str)


# Reverse a string by using function. for eg: vandana -> anadnav
# def reverse(str):
#     reverse_str = ""
#     for c in str:
#         reverse_str = c + reverse_str  # for every character, we are doing concatenation.
#     return reverse_str
#
#
# result = reverse("Vandana")
# print(result)
# result = reverse("Sharma")
# print(result)
# result = reverse("Anjum")
# print(result)
# result = reverse("Chopra")
# print(result)

# To Find a string is palindrome or not. for eg: Naman = naman
# If str (simple string) is equal to reverse of str: str=reverse_str (both are equal) then it's a palindrome.
# palindrome=> str=reverse_str
# original_str = input("Enter any string\n")
# original_str = original_str.lower()
# reverse_str = ""
# for c in original_str:
#     reverse_str = c + reverse_str
# if original_str == reverse_str:
#     print("String is a Palindrome")
# else:
#     print("String is not a Palindrome")


# To Find a string is palindrome or not by using function.
def reverse(original_str):
    reverse_str = ""
    for c in original_str:
        reverse_str = c + reverse_str
    return reverse_str


original_str = input("Enter any string\n")
original_str = original_str.lower()
rev_str = reverse(original_str)
print(rev_str)


if original_str != rev_str:
    print("String is not a Palindrome")
else:
    print("String is a Palindrome")

