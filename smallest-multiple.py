counter = 20

def check():
    for i in range(3, 20):
        if counter % i != 0:
            print(counter, ":", i)
            return False
    print(counter)
    return True


while(True):
    if check():
        break
    counter += 20
