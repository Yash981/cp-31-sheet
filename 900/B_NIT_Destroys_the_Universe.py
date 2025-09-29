from itertools import groupby
t = int(input())
for i in range(t):
    n = int(input())
    arr = list(map(int,input().split()))
    if sum(arr) == 0:
        print(0)
        continue
    groups = 0
    curr = 0
    for key,group in groupby(arr):
        if key != 0:
            curr += 1
        else:
            if curr > 0:
                groups += 1
                curr = 0
    if curr > 0:
        groups += 1
    print(1 if groups == 1 else 2)