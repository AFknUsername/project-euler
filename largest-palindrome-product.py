import math


result = 0


def check_palindrome(n, l):
       s = str(n)
       part1 = s[0:l//2]
       part2 = s[l//2:l][::-1] 
       if part1 == part2:
           return True
       else:
           return False


for i in range(100,1000):
    for j in range(100,1000):
        num = i*j
        l = len(str(num))
        if l % 2 == 0:
            if check_palindrome(num, l):
                if num > result:
                    result = num
                    print(result)
