import math
class sparseTable:
    def __init__(self,arr):
        self.n = len(arr)
        self.arr = arr
        self.log = [0] * (self.n + 1)
        for i in range(2, self.n + 1):
            self.log[i] = self.log[i // 2] + 1
        self.K = self.log[self.n] + 1
        self.st = [[0] * self.K for _ in range(self.n)]
        for i in range(self.n):
            self.st[i][0] = arr[i]
        for j in range(1, self.K):
            for i in range(self.n - (1 << j) + 1):
                self.st[i][j] = math.gcd(self.st[i][j - 1], self.st[i + (1 << (j - 1))][j - 1])
    def query(self, l, r):
        j = self.log[r - l + 1]
        return math.gcd(self.st[l][j], self.st[r - (1 << j) + 1][j])
t = int(input())
for _ in range(t):
    n,q = map(int,input().split())
    a = list(map(int,input().split()))
    diff = []
    for i in range(1,n):
        diff.append(abs(a[i]-a[i-1]))
    st = sparseTable(diff)
    ans = []
    for _ in range(q):
        l,r = map(int,input().split())
        l -= 1
        r -= 1
        if l == r:
            ans.append(0)
        else:
            ans.append(st.query(l,r-1))
    print(*ans)
        
        