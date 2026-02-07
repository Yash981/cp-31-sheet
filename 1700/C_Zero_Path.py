# @lru_cache(None)
# def dp(i,j,cost):
#     if i == n-1 and j == m-1:
#         cost += grid[i][j]
#         return cost == 0
#     if i >= n or j >= m:
#         return False
#     right = dp(i,j+1,cost+grid[i][j])
#     down =  dp(i+1,j,cost+grid[i][j])
#     if right or down:
#         return True
#     return False
# res = dp(0,0,0)
# dp.cache_clear()
# print("YES" if res else "NO")
from functools import lru_cache
t = int(input())
for _ in range(t):
    n,m = map(int,input().split())
    grid = []
    for i in range(n):
        arr = list(map(int,input().split()))
        grid.append(arr)
    if (n+m-1) % 2 == 1:
        print("NO")
        continue
    # @lru_cache(None)
    # def dpMinSum(i,j):
    #     if i == n-1 and j == m-1:
    #         return grid[i][j]
    #     right = 1e9
    #     down = 1e9
    #     if j+1 < m:
    #         right =  dpMinSum(i,j+1)
    #     if i+1 < n:
    #         down = dpMinSum(i+1,j)
    #     return grid[i][j] + min(right,down)
    # res1 = dpMinSum(0,0)
    # dpMinSum.cache_clear()
    # @lru_cache(None)
    # def dpMaxSum(i,j):
    #     if i == n-1 and j == m-1:
    #         return grid[i][j]
    #     right = -1e9
    #     down = -1e9
    #     if j+1 < m:
    #         right =  dpMaxSum(i,j+1)
    #     if i+1 < n:
    #         down = dpMaxSum(i+1,j)
    #     return grid[i][j] + max(right,down)
    # res2 = dpMaxSum(0,0)
    # dpMaxSum.cache_clear()
    dpMinSum = [[1e9 for _ in range(m)] for _ in range(n)]
    dpMinSum[0][0] = grid[0][0]
    for i in range(1,m):
        dpMinSum[0][i] = dpMinSum[0][i-1] + grid[0][i]
    for i in range(1,n):
        dpMinSum[i][0] = dpMinSum[i-1][0] + grid[i][0]
    for i in range(1,n):
        for j in range(1,m):
            right = 1e9
            down = 1e9
            if j > 0:
                right = grid[i][j] + dpMinSum[i][j-1]
            if i > 0:
                down = grid[i][j] + dpMinSum[i-1][j]
            dpMinSum[i][j] = min(right,down)
    # print(dpMinSum)
    dpMaxSum = [[-1e9 for _ in range(m)] for _ in range(n)]
    dpMaxSum[0][0] = grid[0][0]
    for i in range(1,m):
        dpMaxSum[0][i] = dpMaxSum[0][i-1] + grid[0][i]
    for i in range(1,n):
        dpMaxSum[i][0] = dpMaxSum[i-1][0] + grid[i][0]
    for i in range(1,n):
        for j in range(1,m):
            right = -1e9
            down = -1e9
            if j > 0:
                right = grid[i][j] + dpMaxSum[i][j-1]
            if i > 0:
                down = grid[i][j] + dpMaxSum[i-1][j]
            dpMaxSum[i][j] = max(right,down)
    # print(dpMaxSum)

    if dpMinSum[n-1][m-1] <= 0 <= dpMaxSum[n-1][m-1]:
        print("YES")
    else:
        print("NO")
        