
from collections import defaultdict


t = int(input())
for _ in range(t):
    n,m = map(int, input().split())
    rCounter = defaultdict(list)
    
    for _ in range(m):
        a,b = map(int, input().split())
        a -= 1
        b -= 1
        if a > b:
            a, b = b, a
        if b in rCounter:
            rCounter[b][0] = max(rCounter[b][0], a+1)
        else:
            rCounter[b].append(a+1)
    i = 0
    j = 0
    ans = 0
    while j < n:
        if j in rCounter:
            i = max(i, rCounter[j][0])
            i = min(i,j)
        ans += (j-i+1)
        j += 1
    print(ans)
        
            
    
            
