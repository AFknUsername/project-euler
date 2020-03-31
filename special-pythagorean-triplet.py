import math

for i in range(1,1000):
    for j in range(i+1,1000):
        k = 1000 - i - j
        if k > j:
            if i**2 + j**2 == k**2:
                print(i*j*k)
                break
