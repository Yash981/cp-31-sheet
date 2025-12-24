import math
t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int,input().split()))
    currGCD = None
    i = 0
    j = n-1
    while i < j:
        val1 = arr[i]
        val2 = arr[j]
        if abs(val1-val2) != 0:
            if currGCD is None:
                currGCD = abs(val1-val2)
            else:
                currGCD = math.gcd(currGCD,abs(val1-val2))
        i += 1
        j -= 1
    if currGCD is None:
        print(0)
    else:
        print(currGCD)