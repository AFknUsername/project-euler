import math

n = 1
increment = 2
while True:
    count = 0
    for x in range(1, math.floor(math.sqrt(n)) + 1):
        if n % x == 0:
            count += 1
    if count > 250:
        print(n)
        break
    else:
        n = n + increment
        increment += 1


