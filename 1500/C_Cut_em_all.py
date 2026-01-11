from collections import defaultdict
import sys
n = int(input())
if n % 2 == 1:
    print(-1)
    sys.exit()
edges = defaultdict(list)
for _ in range(n-1):
    a,b = map(int,input().split())
    edges[a].append(b)
    edges[b].append(a)
subtree_size = [0]*(n+1)
visited = [False]*(n+1)
# def dfs(node):
#     visited[node] = True
#     size = 1
#     for neighbor in edges[node]:
#         if neighbor != node and not visited[neighbor]:
#             size += dfs(neighbor)
#     subtree_size[node] = size
#     return size
# dfs(1)
stack = []
stack.append((1,0,0))
while stack:
    node,parent,state = stack.pop()
    if state == 0:
        visited[node] = True
        stack.append((node,parent,1))
        for neighbour in edges[node]:
            if neighbour != parent and not visited[neighbour]:
                stack.append((neighbour,node,0))
    else:
        size = 1
        for neighbour in edges[node]:
            if neighbour != parent:
                size += subtree_size[neighbour]
        subtree_size[node] = size
subtree_size = subtree_size[2:]
print(sum(1 for size in subtree_size if size % 2 == 0))