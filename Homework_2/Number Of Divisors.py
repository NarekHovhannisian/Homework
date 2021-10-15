# Number Of Divisors
def divisors(num):
    count = 1
    for i in range(1, num // 2 + 1):
        if num % i == 0:
            count += 1
    return count


x = int(input())
print(divisors(x))
