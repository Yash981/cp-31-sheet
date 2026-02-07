from math import gcd

t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int,input().split()))
    arr.sort()
    flag = False
    for i in range(n):
        if arr[i] % 2 != 0:
            flag = True
            break
    if flag:
        print(2)
        continue
    ans = -1
    for j in range(3,10**5+1,2):
        for jj in range(n):
            if arr[jj] % j != 0 and gcd(arr[jj] , j) == 1:
                ans = j
                flag = True
                break
        if flag:
            break
    print(ans)