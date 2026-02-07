from collections import defaultdict
from itertools import accumulate


t = int(input())
for _ in range(t):
    n = int(input())
    graph = defaultdict(list)
    for _ in range(n-1):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        graph[u].append(v)
        graph[v].append(u)
    depth = [0] * n
    stack = [0]
    visited = [False] * n
    #Pre-order DFS to find depth[node] for every node
    visited[0] = True
    while stack:
        node = stack.pop()
        for neighbor in graph[node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                depth[neighbor] = depth[node] + 1
                stack.append(neighbor)
    #find order of nodes in post-order
    visited = [False] * n
    stack = []
    order = []
    stack.append(0)
    visited[0] = True
    while stack:
        node = stack.pop()
        order.append(node)
        for neighbor in graph[node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                stack.append(neighbor)
    order.reverse()
    #Post-order DFS to find maxDepth[node] for every node
    #find maxDepth for every node contributing to depth
    maxDepth = [0] * n
    for node in order:
        mx = -1
        for neighbor in graph[node]:
            if depth[neighbor] > depth[node]:
                mx = max(mx, maxDepth[neighbor])
        maxDepth[node] = max(depth[node], mx if mx != -1 else 0)
    maxD = max(maxDepth)
    diff = [0] * (maxD + 2)
    for node in range(n):
        diff[depth[node]] += 1
        diff[maxDepth[node] + 1] -= 1
    prefix_sum = list(accumulate(diff))
    ans = n
    for d in prefix_sum[:-1]:
        ans = min(ans,n-d)
    print(ans)
        
