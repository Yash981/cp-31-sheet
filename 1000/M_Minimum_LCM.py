import math
t = int(input())
for _ in range(t):
    n = int(input())
    i = 1
    j = n-1
    ans = float('inf')
    points = [1,n-1]
    print(1,int(n**0.5)+1,"res")
    for d in range(1,int(n**0.5)+1):
        if n % d == 0:
            i = d
            j = n-d
            curLCM = math.lcm(i,j)
            if ans > curLCM:
                ans = curLCM
                points = [i,j]
            ii = n//d
            jj = n - n//d
            if ii > 0 and jj > 0:
                curLCM2 = math.lcm(ii,jj)
                if ans > curLCM2:
                    ans = curLCM2
                    points = [ii,jj]
    print(*points)

