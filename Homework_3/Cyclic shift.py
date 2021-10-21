# Cyclic shift
N = int(input())
k = int(input())
lst = []

for _ in range(N):
    lst.append(int(input()))

k %= N
lst = lst[N-k:] + lst[:N-k]

for item in lst:
    print(item, end=' ')
