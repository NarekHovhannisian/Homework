# The Goldbach Conjecture
def prime(num):
    if num >= 2:
        for i in range(2, (num // 2) + 1):
            if num % i == 0:
                return False
    else:
        return False
    return True


n = int(input())
if 2 < n <= 10000 and n % 2 == 0:
    a, b = 2, n - 2
    while a <= n // 2:
        if prime(a) and prime(b):
            print(a, b)
            break
        else:
            a += 1
            b = n - a
else:
    print("Number should be even number greater than 2 and not exceeding 10000")
