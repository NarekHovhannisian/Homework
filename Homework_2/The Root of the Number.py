# The Root of the Number
def sum_of_digits(x):
    s = 0
    while x:
        s += x % 10
        x //= 10
    return s


a = int(input())
while a > 9:
    print(a)
    a = sum_of_digits(a)
print(a)
