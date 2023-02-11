a = [1, 2, 3]
print(id(a))
b = a
print(id(b))
c = [1, 2, 3]
print(id(c))
print(a == b, a is b, id(a) == id(b))
print(a == c, a is c, id(a) == id(c))
print(id(None))
print(id(False))
print(id(True))
