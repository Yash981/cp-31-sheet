t = int(input())
for _ in range(t):
    n,m = map(int, input().split())
    arr1 = list(map(int, input().split()))
    arr2 = list(map(int, input().split()))
    arr1.append(1)
    arr1.sort()
    arr2.sort()
    i = 0
    j = 0
    while i < n and j < n:
        if arr1[i] < arr2[j]:
            i += 1
            j += 1
        else:
            j += 1
    print(n-i)
    