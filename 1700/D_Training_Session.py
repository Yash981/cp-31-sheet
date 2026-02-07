from collections import Counter
import math


t = int(input())
for _ in range(t):
    n = int(input())
    arr = []
    for _ in range(n):
        a,b = map(int,input().split())
        arr.append([a,b])
    total = math.comb(n,3)
    freqTopic = Counter([x for x,_ in arr])
    freqDifficulty = Counter([y for _,y in arr])
    for i in range(n):
        aa = freqTopic[arr[i][0]] - 1
        bb = freqDifficulty[arr[i][1]] - 1
        total -= (aa * bb)
    print(total)

