import math
t = int(input())
for _ in range(t):
    n,k = map(int,input().split())
    if n <= k:
        print(1)
    else:
        ans = 0
        for i in range(1, int(math.sqrt(n))+1):
            if n % i == 0:
                if n//i <= k:
                    ans = max(ans,n//i)
                if i <= k:
                    ans = max(ans, i)
        print(n//ans)
