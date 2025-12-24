from bisect import bisect_left, bisect_right
from collections import defaultdict
from itertools import accumulate


t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int,input().split()))
    ht = defaultdict(list)
    for i in range(n):
        ht[arr[i]].append(i)
    arr.sort()
    pref = list(accumulate(arr))
    ans = [0] * n
    for i in range(n):
        prefix = pref[i]
        index = bisect_right(arr,prefix) - 1
        index = max(i,index)
        ans[ht[arr[i]].pop(0)] = index
    print(*ans)