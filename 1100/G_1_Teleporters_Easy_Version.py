t = int(input())
for _ in range(t):
    n,k = map(int,input().split())
    arr = list(map(int,input().split()))
    sortyArr = []
    for i in range(n):
        sortyArr.append(arr[i]+i+1)
    sortyArr.sort()
    teleports = 0
    x = 0
    while x < n and sortyArr and k-sortyArr[x] >= 0:
        teleports += 1
        k -= sortyArr[x]
        x += 1
    print(teleports)
        
