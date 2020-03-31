import math


list = [3, 5]
current = 7

while (True):
    limit = math.ceil(current/2)
    for x in range(len(list)):
        if list[x] > limit:
            list.append(current)
            print(current)
            break
        if (current % list[x] == 0):
            break
    if len(list) == 10000:
        break
    current += 2
print(list[-1])
