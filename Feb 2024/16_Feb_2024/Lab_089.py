# Till now, we have seen, dictionary is not in order
# but there is module name i.e. "Collections" and we create a OrderedDict
# Ordered dictionary is used sometimes when we need to keep order as it is.
# Ordered dictionary is also a key value pair, but it will maintain order.
from collections import OrderedDict

od = OrderedDict()
od['a'] = 100
od["b"] = 78
od['c'] = 97
od["d"] = 31
print(od)
print(list(od))
print(tuple(od))
print(set(od))
print(dict(od))

# Dict-> It will not keep the Order of insertion
# OrderedDict-> It will keep the order of insertion
