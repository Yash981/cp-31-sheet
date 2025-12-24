t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int,input().split()))
    if all(x < 0 for x in arr):
        print(max(arr))
        continue
    ans = max(arr)
    currsum = 0
    prev = 1-(arr[0] % 2)
    for i in range(n):
        if currsum < 0:
            currsum = 0
        if prev != arr[i] % 2:
            currsum += arr[i]
            prev = arr[i] % 2
        else:
            prev = arr[i] % 2
            currsum = arr[i]
        ans = max(currsum,ans)
    print(ans)

