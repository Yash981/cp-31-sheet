from collections import defaultdict,deque
import sys
input =  sys.stdin.readline
t = int(input())
for _ in range(t):
    n = int(input())
    graph = defaultdict(list)
    adjacencylist = defaultdict(list)
    for i in range(n):
        l,r = map(int,input().split())
        graph[i+1].append([l,r])
    for _ in range(n-1):
        u,v = map(int,input().split())
        adjacencylist[u].append(v)
        adjacencylist[v].append(u)
    # @lru_cache(None)
    # def dp(node,parent):
    #     L, R = graph[node][0]
    #     parentL = 0
    #     parentR = 0
    #     for child in adjacencylist[node]:
    #         if child == parent:
    #             continue
    #         cL, cR = graph[child][0]
    #         childL, childR = dp(child,node)
    #         parentL += max(abs(cL - L)+childL, abs(cR - L)+childR)
    #         parentR += max(abs(cL - R)+childL, abs(cR - R)+childR)
    #     return parentL, parentR
    # maxL,maxR = dp(1,0)
    # dp.cache_clear()
    # print(max(maxL,maxR))

    dpL = [0] * (n+1)
    dpR = [0] * (n+1)
    queue = deque([1])
    parent = [0] * (n+1)
    order = []
    while queue:
        node = queue.popleft()
        order.append(node)
        for child in adjacencylist[node]:
            if child == parent[node]:
                continue
            parent[child] = node
            queue.append(child)
    # print(parent,order)
    for node in reversed(order):
        parent_node = parent[node]
        L, R = graph[node][0]
        nodeLeft = 0
        nodeRight = 0
        for child in adjacencylist[node]:
            if child == parent_node:
                continue
            queue.append((child,node))
            cL, cR = graph[child][0]
            childL, childR = dpL[child], dpR[child]
            nodeLeft += max(abs(cL - L)+childL, abs(cR - L)+childR)
            nodeRight += max(abs(cL - R)+childL, abs(cR - R)+childR)
        dpL[node] = nodeLeft
        dpR[node] = nodeRight
    print(max(dpL[1],dpR[1]))