import functools
import operator


t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int,input().split()))
    print(functools.reduce(operator.and_,arr))