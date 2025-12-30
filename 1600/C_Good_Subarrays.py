
from collections import Counter

t = int(input())
for _ in range(t):
    n = int(input())
    s = [int(x)-1 for x in input()]
    prefix = 0
    hashmap = Counter()
    hashmap[0] = 1
    ans = 0
    for i in range(n):
        prefix += s[i]
        if prefix in hashmap:
            ans += hashmap[prefix]
        hashmap[prefix] += 1
    print(ans)
    
    