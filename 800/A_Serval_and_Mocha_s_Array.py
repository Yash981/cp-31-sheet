from math import gcd


t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int,input().split()))
    if n <= 2:
        print("No")
    else:
        flag = False
        for x in range(n):
            for y in range(n):
                if x == y:continue
                if gcd(arr[x],arr[y]) <= 2:
                    print("Yes")
                    flag = True
                    break
            if flag:
                break
        if not flag:
            print("No")