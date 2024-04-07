def make_pizza(*tops, base):
    print(tops, base)
    for top in tops:
        print(top)
    return tops, base # We can also return multiple things by comma separated in python but in JAVA it's super difficult


vandana_t, vandana_b = make_pizza("onion", "tomato", "sweetcorn", base='thin crust')
print(vandana_t)
print(vandana_b)

