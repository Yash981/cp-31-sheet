t = int(input())
MAXX = 4 * (10**4)
MOD = 10**9 + 7
palindromes = []
for i in range(1,MAXX+1):
    s = str(i)
    if s == s[::-1]:
        palindromes.append(i)
queries = [int(input()) for _ in range(t)]
    # @lru_cache(None)
    # def dp(x,last_index_used):
    #     if x == n:
    #         return 1
    #     if x > n:
    #         return 0
    #     ans = 0
    #     for i in range(last_index_used,len(palindromes)):
    #         if x+palindromes[i] > n:
    #             break
    #         ans += dp(x+palindromes[i],i)
    #         ans %= MOD
    #     return ans
    # print(dp(0,0) % MOD)

MAXQ = max(queries)
DP = [0] * (MAXQ+1)
DP[0] = 1
for p in palindromes:
    if p > MAXQ:
        break
    for i in range(MAXQ-p+1):
        DP[i+p] += DP[i]
        DP[i+p] %= MOD
for q in queries:
    print(DP[q] % MOD)