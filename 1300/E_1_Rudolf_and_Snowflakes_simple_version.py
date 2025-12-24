import math
t = int(input())
for _ in range(t):
    n = int(input())
    if n <= 3:
        print("NO")
        continue
    for i in range(2,math.ceil(math.sqrt(n))+1):
        currAns = 1
        j = 1
        while currAns < n:
            currAns += i**j
            j += 1
        if currAns == n:
            print("YES")
            break
    else:
        print("NO")
