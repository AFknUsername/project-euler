arr = [1,2,3]
sum = 2
while (True):
    temp = arr[1]+arr[2]
    if temp > 4000000:
        print(sum)
        break
    if temp%2 == 0:
        sum += temp
    arr[0]=arr[1]
    arr[1]=arr[2]
    arr[2]=temp
