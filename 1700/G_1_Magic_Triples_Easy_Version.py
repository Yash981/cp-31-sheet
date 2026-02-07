from collections import Counter
import sys
input = sys.stdin.readline
from math import sqrt
t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int,input().split()))
    freq = Counter(arr)
    ans = 0
    #same values
    for key,value in freq.items():
        if value >= 3:
            ans += value*(value-1)*(value-2) #factorial(value)//(factorial(value-3))
    #multiples
    mx = max(arr)
    for key in freq.keys():
        mul = 2
        while key * mul * mul <= mx:
            factor2 = freq[key*mul]
            if factor2 > 0:
                factor3 = freq[key*mul*mul]
                if factor3 > 0:
                    ans += freq[key] * factor2 * factor3
            mul += 1
        # for mul in range(2, int(sqrt(mx // key)) + 1):
        #     if freq[key*mul] > 0 and freq[key*mul*mul] > 0:
        #         ans += (freq[key] * freq[key*mul] * freq[key*mul*mul])
    print(ans)