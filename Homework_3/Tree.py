# Tree
n = int(input())
spaces = n // 2
stars = 1
while stars <= n:
    print(spaces * ' ', stars * '*', sep='')
    spaces -= 1
    stars += 2
