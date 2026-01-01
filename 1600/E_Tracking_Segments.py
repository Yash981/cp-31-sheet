
from itertools import accumulate

t = int(input())
for _ in range(t):
    n,m = map(int,input().split())
    segments = []
    for _ in range(m):
        l,r = map(int,input().split())
        segments.append((l,r))
    q = int(input())
    queries = []
    for _ in range(q):
        query = int(input())
        queries.append(query)
    def isPossible(mid):
        empty = [0] * n
        for i in range(mid+1):
            query = queries[i]
            query -= 1
            empty[query] = 1 - empty[query]
        prefix = [0] + list(accumulate(empty))
        for i in range(m):
            l,r = segments[i]
            l -= 1
            r -= 1
            length = ((r-l+1)//2)+1
            if prefix[r+1] - prefix[l] >= length:
                return True
        return False

            
    left = 0
    right = q-1
    ans = -1
    while left <= right:
        mid = left + (right-left)//2
        if isPossible(mid):
            ans = mid + 1
            right = mid-1
        else:
            left = mid+1
    print(ans)