# Digit Product
a = int(input())
product = 1
while a > 0:
    if a % 10 != 0:
        product *= a % 10
    a //= 10
print(product)
