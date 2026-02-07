t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    INF = float('inf')
    dp = [INF] * (n+1)
    present = [False] * (n+1)
    for i in range(n):
        present[arr[i]] = True
    for i in range(1, n+1):
        if present[i]:
            dp[i] = 1
    for i in range(1,n+1):
        if dp[i] == INF:
            continue
        for j in range(1, n//i + 1):
            if present[j]:
                dp[i*j] = min(dp[i*j], dp[i] + 1)
    print(*[x if x != INF else -1 for x in dp[1:]])