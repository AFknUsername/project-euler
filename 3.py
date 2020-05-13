import math


num = 600851475143
limit = num // 2
result = 0


def compare(n, result):
    if n > result:
        result = n
        print(result)


def is_prime(n):
    for i in range(2, n):
        if (n % i) == 0:
            return False
    return True


for i in range(2, limit): 
    if (num % i) == 0:
        if is_prime(i):
            compare(i, result)
print('done')
