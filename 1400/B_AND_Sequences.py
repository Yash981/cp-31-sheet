from collections import Counter
import math
t = int(input())
mod = 10**9+7
for _ in range(t):
    n = int(input())
    arr = list(map(int,input().split()))
    totalAnd = arr[0]
    for i in arr[1:]:
        totalAnd &= i
    freq = Counter(arr)
    if freq[totalAnd] <= 1:
        print(0)
        continue
    print((freq[totalAnd] * (freq[totalAnd]-1) * math.factorial(n-2)) % mod)