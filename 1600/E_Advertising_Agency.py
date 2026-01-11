from collections import Counter
import math
t = int(input())
mod = 10**9+7
for _ in range(t):
    n,k = map(int,input().split())
    arr = list(map(int,input().split()))
    arr.sort(reverse=True)
    values = arr[:k]
    currValFreq = Counter(values)
    freq = Counter(arr)
    ans = 1
    for x,val in currValFreq.items():
        ans *= math.comb(freq[x],val)
        ans %= mod
    print(ans % mod)
        

