current = 0
highest = 0
result = 0
temp = 0

def do_the_thing(n):
    global current
    global highest
    global result
    global temp
    current += 1
    if n == 1:
#        print(("{} : {}").format(temp, current))
        if current > highest:
            highest = current
            result = temp
        current = 0
    elif n%2==0:
        do_the_thing(n/2)
    else:
        do_the_thing(3*n+1)


for x in range(1,1000001):
    temp = x
    do_the_thing(x)

print(result)
