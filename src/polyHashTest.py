def polyHash(attribute):
    p=31
    x = 8
    hash = 0
    for i in range(len(attribute)-1,-1, -1):
        hash = (hash*x+ord(attribute[i]))%p
    return hash

print(polyHash("Yellow"))
print(polyHash("Red"))
print(polyHash("Green"))
print(polyHash("Blue"))
print(polyHash("Black"))
print(polyHash("power"))
print(polyHash("+2"))
print(polyHash("+4"))
print(polyHash("change_color"))
print(polyHash("Reverse"))
print(polyHash("Block"))
