
from functools import lru_cache

t = int(input())
MAXX = 4 * (10**4)
MOD = 10**9 + 7
palindromes = []
for i in range(1,MAXX+1):
    s = str(i)
    if s == s[::-1]:
        palindromes.append(i)
queries = [int(input()) for _ in range(t)]
hashmap = {}
for i in range(t):
    hashmap[queries[i]] = i
queries = sorted(queries)
memo = {}
def dp(x,last_index_used,q):
    if x == q:
        return 1
    if x > q:
        return 0
    if (x,last_index_used) in memo:
        return memo[(x,last_index_used)]
    ans = 0
    for i in range(last_index_used,len(palindromes)):
        if x+palindromes[i] > q:
            break
        ans += dp(x+palindromes[i],i,q)
        ans %= MOD
    memo[(x,last_index_used)] = ans
    return ans
res = [0] * len(queries)
for i in queries:
    res[hashmap[i]] = dp(0,0,i) % MOD
for i in res:
    print(i)
print(memo)
# for q in queries:
#     print(dp(0,0,q) % MOD)
# MAXQ = max(queries)
# DP = [0] * (MAXQ+1)
# DP[0] = 1
# for p in palindromes:
#     if p > MAXQ:
#         break
#     for i in range(MAXQ-p+1):
#         DP[i+p] += DP[i]
#         DP[i+p] %= MOD
# for q in queries:
#     print(DP[q] % MOD)