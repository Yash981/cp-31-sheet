t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    i = 0
    j = n-1
    mn = 1
    mx = n
    while (i <= j):
        if arr[i] == mn:
            i += 1
            mn += 1
        elif arr[j] == mx:
            j -= 1
            mx -= 1
        elif arr[i] == mx:
            i += 1
            mx -= 1
        elif arr[j] == mn:
            j -= 1
            mn += 1
        else:
            break
    if i > j:
        print(-1)
    else:
        print(i+1, j+1)
            