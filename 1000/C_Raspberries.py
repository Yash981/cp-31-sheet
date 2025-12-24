import math
t = int(input())
for _ in range(t):
    n,k = map(int,input().split())
    arr = list(map(int,input().split()))
    ans =  0 if math.prod(arr) % k == 0 else 1e9
    even = 0
    for i in arr:
        if i % 2 == 0:
            even += 1
        ans = min(ans,k-i%k)
    if k == 4:
        if even >= 2:
            ans = min(ans,0)
        elif even == 1:
            ans = min(ans,1)
        else:
            ans = min(ans,2)

    print(ans)