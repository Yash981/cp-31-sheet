t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int,input().split()))
    i = n-1
    suffix = 0
    while i >= 0 and arr[i] == arr[-1]:
        suffix += 1
        i -= 1
    if i < 0:
        print(0)
        continue
    i -= suffix
    ans = 1
    while i >= 0:
        if arr[i] == arr[-1]:
            i -= 1
            continue
        ans += 1
        i -= ((n-1)-i)
    print(ans)