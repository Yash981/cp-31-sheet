t = int(input())
for _ in range(t):
    a,b,n = map(int,input().split())
    arr = list(map(int,input().split()))
    ans = b
    for x in range(n):
        ans += min(arr[x],a-1)
    print(ans)