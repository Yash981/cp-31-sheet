from collections import Counter
import math
t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    freq = Counter(s)
    print(freq)
    factors = []
    for i in range(1,math.ceil(math.sqrt(n))):
        if n%i == 0:
            factors.append(i)
            factors.append(n//i)
    factors.sort()
    print(factors)
    ans = n
    best_ans = n
    for x in factors:
        keep = 0
        for key,value in freq.items():
            keep += min(value,n//x)
        if ans > n-keep:
            ans = n-keep
            best_ans = x
    print(ans,best_ans)