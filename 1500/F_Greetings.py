class Fenwick:
    def __init__(self, n):
        self.n = n
        self.bit = [0] * (n + 1)

    def update(self, i, delta=1):
        # add delta at index i (1-based)
        while i <= self.n:
            self.bit[i] += delta
            i += i & -i

    def query(self, i):
        # sum from 1 to i (1-based)
        s = 0
        while i > 0:
            s += self.bit[i]
            i -= i & -i
        return s

    def range_query(self, l, r):
        return self.query(r) - self.query(l - 1)
t = int(input())
for tt in range(t):
    n = int(input())
    arr = []
    for _ in range(n):
        a,b = map(int,input().split())
        arr.append([a,b])
    arr.sort()
    destination = [y for x,y in arr]
    vals = sorted(set(destination))
    comp = {v: i+1 for i, v in enumerate(vals)}
    fw = Fenwick(len(vals))
    #[100, 8, 6, 9, 5, 10]
    ans = 0
    for x in range(n-1,-1,-1):
        x = comp[destination[x]]
        ans += fw.query(x-1)
        fw.update(x, 1)
    print(ans)