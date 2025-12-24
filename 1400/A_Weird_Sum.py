from collections import defaultdict

n,m = map(int, input().split())
grid = []
for _ in range(n):
    grid.append(list(map(int, input().split())))
def sum_abs(arr):
    arr.sort()
    prefix = 0
    res = 0
    for i, coordinate in enumerate(arr):
        res += coordinate * i - prefix
        prefix += coordinate
    return res

ht = defaultdict(list)

for i in range(n):
    for j in range(m):
        color = grid[i][j]
        ht[color].append((i, j))

ans = 0

for color, cells in ht.items():
    if len(cells) <= 1:
        continue

    xs = [x for x, y in cells]
    ys = [y for x, y in cells]

    ans += sum_abs(xs)
    ans += sum_abs(ys)

print(ans)
