from collections import Counter
from math import gcd

n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
freq = Counter()
count = 0

for i in range(n):
    if a[i] == 0:
        if b[i] == 0:
            count += 1
    else:
        x = -b[i]
        y = a[i]
        
        common = gcd(x, y)
        x //= common
        y //= common
        
        if y < 0:
            x = -x
            y = -y
            
        freq[(x, y)] += 1

print(count + max(freq.values(), default=0))