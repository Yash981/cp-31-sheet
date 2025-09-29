t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int,input().split()))
    index = n-2
    prev = arr[n-1]
    ans = 0
    while index >= 0:
        curr = arr[index]
        while curr > 0 and curr >= prev:
            curr = curr//2
            ans += 1
        arr[index] = curr
        prev = arr[index]
        index -= 1
    if len(arr) != len(set(arr)): print(-1)
    else: print(ans)