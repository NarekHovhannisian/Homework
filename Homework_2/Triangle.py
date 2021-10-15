# Triangle
def triangle_type(x, y, z):
    if z < x:
        z, x = x, z
    elif z < y:
        z, y = y, z  # Now z is the largest
    if x + y <= z:
        return "No Triangle"
    if x ** 2 + y ** 2 == z ** 2:
        return "Right Triangle"
    elif x ** 2 + y ** 2 < z ** 2:
        return "Obtuse Triangle"
    else:
        return "Acute Triangle"


a = int(input())
b = int(input())
c = int(input())
print(triangle_type(a, b, c))
