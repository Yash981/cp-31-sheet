from collections import Counter
class DSU:
    def __init__(self,n):
        self.parent = list(range(n))
        self.rank = [1]*n
    def find(self,x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    def union(self,x,y):
        px,py = self.find(x),self.find(y)
        if px == py:
            return
        if self.rank[px] < self.rank[py]:
            px,py = py,px
        self.parent[py] = px
        self.rank[px] += self.rank[py]

def solve():
    n,m = map(int,input().split())
    dsu = DSU(n)
    ans = []
    for _ in range(m):
        k, *users = list(map(int, input().split()))
        for i in range(k-1):
            dsu.union(users[i]-1,users[i+1]-1)
    freq = Counter()
    for i in range(n):
        freq[dsu.find(i)] += 1
    for i in range(n):
        ans.append(freq[dsu.parent[i]])
    print(*ans)
solve()
        
        
    