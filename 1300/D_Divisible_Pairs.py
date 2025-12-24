from collections import defaultdict
from typing import Counter


t = int(input())
for _ in range(t):
    n,x,y = map(int,input().split())
    arr = list(map(int,input().split()))
    ht = Counter()
    ans = 0
    for i in range(n):
        remY = arr[i] % y
        remX = arr[i] % x
        need = (x-remX) % x
        ans += ht[(remY,need)]
        ht[(remY,remX)] += 1
    print(ans)    