t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int,input().split()))
    even = False
    odd = False
    for i in range(n):
        if arr[i] % 2 == 0:
            even = True
        if arr[i] % 2 == 1:
            odd = True
        if even and odd:
            break
    if even and odd:
        arr.sort()
        print(*arr)
    else:
        print(*arr)

    