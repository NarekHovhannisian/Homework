# Digit Sum 3
a = int(input())
s = a % 10 + a // 10 % 10 + a // 100
print(s)
