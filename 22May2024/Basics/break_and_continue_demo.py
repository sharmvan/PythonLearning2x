# break: Breaks out from the nearest enclosing loop
# continue: Go to the start of nearest enclosing loop
#
# while <expression>:
#     <statement(s)>
#     break
#     <statement(s)>
#     continue
#     <statement(s)>
# <statement(s)>
#
# else clause:
# while <expression>:
#     <statement(s)>
# else:
#     <statement(s)>

# i = 0
# s = "The Testing Academy"
# while True:
#     print(s[i])
#     if s[i] == 'i':
#         break
#     i = i + 1
# print("Out of the loop")

i = 0
s = "The Testing Academy"
while i < len(s):
    if s[i] == 'n':
        i = i + 1
        continue
    print(s[i])
    i = i + 1
