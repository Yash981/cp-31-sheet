from collections import defaultdict
from math import ceil,floor


t = int(input())
for _ in range(t):
    n = int(input())
    graph = defaultdict(list)
    leaves = [0] * (n)
    for _ in range(n-1):
        u,v = map(int,input().split())
        u -= 1
        v -= 1
        graph[u].append(v)
        leaves[u] += 1
        leaves[v] += 1
    print("leaves",leaves)
    s = input()
    leavesOnes = 0
    leavesZeros = 0
    def calc():
        global leavesOnes,leavesZeros
        count = 0
        for i in range(1,n):
            if leaves[i] == 1 and ((s[i] == "0" and s[0] == "1") or (s[i] == "1" and s[0] == "0")):
                if s[i] == "0":
                    leavesZeros += 1
                else:
                    leavesOnes += 1
                count += 1
        return count
    fixedCount = calc()
    ans = 0
    if s[0] != "?":
        ans = fixedCount
        leaveCount = 0
        for i in range(1,n):
            if s[i] == "?":
                if leaves[i] == 1:
                    leaveCount += 1
        ans += ceil(leaveCount/2)
        print(ans)
    else:
        #pretend root as 0
        fixedCount1 = leavesOnes
        #pretend root as 1
        fixedCount2 = leavesZeros
        leaveCount = 0
        questionsCount = 0
        for i in range(1,n):
            if s[i] == "?":
                if leaves[i] == 1:
                    leaveCount += 1
                else:
                    questionsCount += 1
        contri = questionsCount % 2  if leavesOnes == leavesZeros else 0
        fixedCount1 += ceil((leaveCount+contri)/2)
        fixedCount2 += ceil((leaveCount+contri)/2)
        print(max(fixedCount1,fixedCount2))



        
    