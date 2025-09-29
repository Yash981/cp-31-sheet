import math
t = int(input())
for _ in range(t):
    n,k = map(int,input().split())
    arr = list(map(int,input().split()))
    length = len(arr)
    median = 0
    if n % 2 == 0:
        median = (n//2)
    else:
        median = math.ceil((n/2))
    index = length - (n-median+1)
    ans = 0
    while k and index >= 0:
        ans += arr[index]
        index -= n-median+1
        k -= 1
    print(ans)