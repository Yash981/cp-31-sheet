t = int(input())
for _ in range(t):
    n,x = map(int,input().split())
    arr = list(map(int,input().split()))
    currStart = arr[0]-x
    currEnd = arr[0]+x
    ans = 0
    for i in range(n):
        if max(currStart,arr[i]-x) <= min(currEnd,arr[i]+x):
            currStart = max(currStart,arr[i]-x)
            currEnd = min(currEnd,arr[i]+x)
        else:
            ans += 1
            currStart = arr[i]-x
            currEnd = arr[i]+x
    print(ans)