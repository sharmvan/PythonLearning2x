# used to iterate over the sequence like list, string, dictionary, set or tuple.
# less like the for loop in other programming language.
city = "Delhi"
for c in city:
    print(c)

cities = ("Delhi", "Bihar", "Punjab", "Kolkata", "Mumbai")
for c in cities:
    print(c)

cities = [["India", "Delhi"], ["Australia", "Melbourne"], ["Canada", "Vancouver"]]
for country, city in cities:
    print(f"{country} -> {city}")

cities = [["India", "Delhi"], ["Australia", "Melbourne"], ["Canada", "Vancouver"]]
my_dictionary = dict(cities)
print(my_dictionary)
for c,s in my_dictionary.items():
    print(c,s)
    for C in c:
        print(C)
