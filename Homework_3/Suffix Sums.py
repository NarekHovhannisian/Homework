# Suffix Sums
a = list(map(float, input().split()))

b = []
for i in range(len(a)):
    s = 0
    for j in range(i, len(a)):
        s += a[j]
    b.append(s)

for item in b:
    print(item, end=' ')
