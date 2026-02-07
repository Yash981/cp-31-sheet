from collections import Counter
from itertools import accumulate
t = int(input())
for _ in range(t):
    n = int(input())
    p = list(map(int, input().split()))
    suffixMax =  list(accumulate(p[::-1], max))[::-1]
    indices = Counter()
    for i in range(n):
        indices[p[i]] = i
    # print(suffixMax)
    # print(indices)
    # print(p)
    for i in range(n):
        if p[i] != suffixMax[i]:
            j = indices[suffixMax[i]]
            p[i:j+1] = p[i:j+1][::-1]
            break
    print(*p)