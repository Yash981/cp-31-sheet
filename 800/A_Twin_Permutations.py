t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int,input().split()))
    B = []
    for i in range(n):
        B.append(n+1-arr[i])
    print(*B)
