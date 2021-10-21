# Palindrome numbers
def reverse(num):
    res = 0
    while num:
        res *= 10
        res += num % 10
        num //= 10
    return res


a, b = int(input()), int(input())
for i in range(a, b + 1):
    if i == reverse(i):
        print(i)
