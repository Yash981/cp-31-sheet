from itertools import groupby


t = int(input())
mod = 998244353
for _ in range(t):
    s = [x for x in input()]
    ans = [0,0]
    res = 0
    for key,grp in groupby(s):
        grouped = list(grp)
        n = len(grouped)
        if n > 1:
            ans[0] += n-1
            ans[1] += ((n-1) * n)
            ans[1] %= mod
            res += 1
    print(*[0,1] if ans==[0,0] else [ans[0],ans[1]*res])
        
