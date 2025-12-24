t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int,input().split()))
    if all(x > 0 for x in arr):
        print("YES")
    else:
        yaseer = sum(arr)
        adelsum = 0
        maxadelsum = 0
        for i in range(n-1):
            if adelsum < 0:
                adelsum = 0
            adelsum += arr[i]
            maxadelsum = max(maxadelsum,adelsum)
        adelsum = 0
        for j in range(1,n):
            if adelsum < 0:
                adelsum = 0
            adelsum += arr[j]
            maxadelsum = max(maxadelsum,adelsum)
        if  yaseer > maxadelsum:
            print("YES")
        else:
            print("NO")
