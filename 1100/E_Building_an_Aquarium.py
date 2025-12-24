t = int(input())
for _ in range(t):
    n,x = map(int,input().split())
    arr = list(map(int,input().split()))
    def isPossible(mid):
        total = 0
        for i in arr:
            if i < mid:
                total += mid-i
        return total <= x
    l = 1
    h = 10**10
    ans = 1
    while l <= h:
        mid = l + (h-l)//2
        if isPossible(mid):
            ans = mid
            l = mid + 1
        else:
            h = mid - 1
    print(ans)