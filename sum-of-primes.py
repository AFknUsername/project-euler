import math
n = 2000000
li = [True for x in range(n)]
s = 0
limit = int(math.ceil(math.sqrt(n)))
li[0] = False
li[1] = False

for x in range(limit):
    if li[x] == False: 
        continue
    else: 
        for i in range(x, n):
            if x*i < n:
                li[x*i] = False
            else:
                break

for x in range(len(li)):
    if li[x]:
        s += x

print(s)
