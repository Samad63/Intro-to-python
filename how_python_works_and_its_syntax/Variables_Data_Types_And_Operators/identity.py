a = 1000
b = a
c = 1000.0
print(type(a), type(c))
print(a == c) # Equal Values
print(a is b) # Same Object
print(id(a) == id(b))
print(a is c)