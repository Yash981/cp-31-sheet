import sys
input = sys.stdin.readline

class Fenwick:
    def __init__(self, n):
        self.bit = [0] * (n + 1)
        self.n = n

    def update(self, i, val):
        while i <= self.n:
            if val > self.bit[i]:
                self.bit[i] = val
            i += i & -i

    def query(self, i):
        res = 0
        while i > 0:
            if self.bit[i] > res:
                res = self.bit[i]
            i -= i & -i
        return res

t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int,input().split()))
    cost = list(map(int,input().split()))

    vals = sorted(set(arr))
    comp = {v: i + 1 for i, v in enumerate(vals)}
    m = len(vals)

    bit = Fenwick(m)
    dp = [0] * n

    for i in range(n):
        val = comp[arr[i]]
        res = bit.query(val) 
        dp[i] = res + cost[i]
        bit.update(val, dp[i])

    mx = max(dp)
    total = sum(cost)
    print(total - mx)