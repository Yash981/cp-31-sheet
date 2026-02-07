from collections import defaultdict


t = int(input())
graph = defaultdict(list)
for _ in range(t):
    n,k = map(int,input().split())
    for _ in range(n):
        u,v = map(int,input().split())
        graph[u].append(v)
        graph[v].append(u)
    print(graph)
