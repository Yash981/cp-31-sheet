from collections import Counter


t = int(input())
for _ in range(t):
    n,cardboard = map(int,input().split())
    arr = list(map(int,input().split()))
    freq = Counter(arr)
    def isPossible(mid):
        size = 0
        for key,val in freq.items():
            size += ((key+(mid*2))**2) * val
        return size <= cardboard
    l = 0
    r = 10**9
    ans = 1e12
    while l <= r:
        mid = l + (r-l)//2
        if isPossible(mid):
            ans = mid
            l = mid + 1
        else:
            r = mid - 1
    print(ans)
    
