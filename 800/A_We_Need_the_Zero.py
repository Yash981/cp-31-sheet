t = int(input())
for i in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    ans = a[0]
    for j in range(1,n):
        ans ^= a[j]
    if ans == 0:
        print(0)
        continue
    # print(ans)
    res = (ans^a[0])
    for k in range(1,n):
        res ^= (ans^a[k])
    # print(res)
    if ans != res:
        print(ans)
    else:
        print(-1)
