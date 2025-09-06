t = int(input())
for _ in range(t):
    n,k = map(int,input().split())
    arr = list(map(int,input().split()))
    arr.sort()
    curr = 0
    ans = 0
    for x in range(n-1):
        if arr[x+1] - arr[x]  <= k:
            curr += 1
        else:
            ans = max(ans,curr+1)
            curr = 0
    ans = max(ans,curr+1)
    print(n-ans)