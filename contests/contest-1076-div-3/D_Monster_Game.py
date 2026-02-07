from bisect import bisect_left, bisect_right
from itertools import accumulate


t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    sortyA = sorted(a)
    prefix = list(accumulate(b))
    # print(sortyA)
    # print(prefix)
    ans = 0
    for i in range(n):
        x = sortyA[i]
        total = n-i
        idx = bisect_right(prefix, total)
        ans = max(ans, x * (idx))
    print(ans)