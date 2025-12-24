t = int(input())
for _ in range(t):
    n,x = map(int,input().split())
    arr1 = list(map(int,input().split()))
    arr2 = list(map(int,input().split()))
    arr3 = list(map(int,input().split()))
    curr = 0
    for val in arr1:
        if (val | x) == x:
            curr |= val
        else:
            break
    for val in arr2:
        if (val | x) == x:
            curr |= val
        else:
            break
    for val in arr3:
        if (val | x) == x:
            curr |= val
        else:
            break
    print("Yes" if curr == x else "No")
    