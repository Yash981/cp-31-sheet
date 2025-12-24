import sys
input = sys.stdin.readline

MAXB = 30  # since ai <= 1e9

def solve():
    n = int(input())
    a = list(map(int, input().split()))

    # 1️⃣ Build prefix bit counts
    # pre[i][b] = count of numbers in a[0..i-1] with bit b set
    pre = [[0] * MAXB for _ in range(n + 1)]

    for i in range(1, n + 1):
        x = a[i - 1]
        for b in range(MAXB):
            pre[i][b] = pre[i - 1][b]
            if (x >> b) & 1:
                pre[i][b] += 1
    print(pre)
    # 2️⃣ Function to compute AND(l, r) using prefix bits
    def range_and(l, r):
        print(l,r)
        length = r - l + 1
        print(length)
        val = 0
        for b in range(MAXB):
            if pre[r][b] - pre[l - 1][b] == length:
                print("before:",1<<b,b)
                val |= (1 << b)
                print("each step",val)
        print("final:",val)
        return val

    # 3️⃣ Process queries
    res = []
    for _ in range(int(input())):
        l, k = map(int, input().split())

        low, high = l, n
        ans = -1

        while low <= high:
            mid = (low + high) // 2
            if range_and(l, mid) >= k:
                ans = mid        # valid, try to go right
                low = mid + 1
            else:
                high = mid - 1
        print("-------")
        res.append(ans)
    print(*res)


# -------- main --------
t = int(input())
for _ in range(t):
    solve()
