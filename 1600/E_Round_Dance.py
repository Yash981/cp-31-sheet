from collections import defaultdict
t = int(input())
for _ in range(t):
    n = int(input())
    s = list(map(int,input().split()))
    freq = defaultdict(set)
    for i,x in enumerate(s):
        freq[x].add(i+1)
        freq[i+1].add(x)
    visited = [0] * (n+1)
    def dfs(start):
        stack = [start]
        visited[start] = 1
        component = []

        while stack:
            node = stack.pop()
            component.append(node)
            for neighbor in freq[node]:
                if visited[neighbor] == 0:
                    visited[neighbor] = 1
                    stack.append(neighbor)

        return component
    allComponents = []
    for i in range(1,n+1):
        if visited[i] == 0:
            allComponents.append(dfs(i))
    
    freeslot = 0
    MinRounds = 0
    for component in allComponents:
        canMerge = False
        for i in component:
            if len(freq[i]) == 1:
                canMerge = True
                break
        if canMerge:
            freeslot += 1
        else:
            MinRounds += 1
    ActualMinRounds = MinRounds + min(freeslot,1)
    ActualMaxRounds = MinRounds + freeslot
    print(ActualMinRounds,ActualMaxRounds)   
    