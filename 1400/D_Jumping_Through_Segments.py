t = int(input())
for _ in range(t):
    n = int(input())
    arr = []
    for _ in range(n):
        l,r = map(int, input().split())
        arr.append([l,r])
    def isPossible(mid):
        currStart = 0
        currEnd = 0
        for i in range(n):
            reachStart = currStart-mid
            reachEnd = currEnd+mid
            currStart = max(arr[i][0],reachStart)
            currEnd = min(arr[i][1],reachEnd)
            if currStart > currEnd:
                return False
        return True

    left = 0
    right = 10**18
    while left <= right:
        mid = left + (right-left)//2
        if isPossible(mid):
            right = mid-1
        else:
            left = mid+1
    print(left)
            

    