from collections import Counter
MOD = 10**9+7
class DSU:
    def __init__(self,n):
        self.parent = list(range(n))
    def find(self,a):
        if self.parent[a] != a:
            self.parent[a] = self.find(self.parent[a])
        return self.parent[a]
    def union(self,a,b):
        pa = self.find(a)
        pb = self.find(b)
        if pa != pb:
            self.parent[pa] = pb
n,k = map(int,input().split())
dsu = DSU(n)
for _ in range(n-1):
    u,v,x = map(int,input().split())
    if x != 1:
        dsu.union(u-1,v-1)
for i in range(n):
    dsu.find(i)
freq = Counter(dsu.parent)
total = pow(n,k,MOD)
for key,value in freq.items():
    res = pow(value,k,MOD)
    total -= res
    total %= MOD
print(total)
