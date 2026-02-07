from collections import Counter


t = int(input())
for _ in range(t):
    n = int(input())
    s,t = map(str,input().split())
    if Counter(s) == Counter(t):
        print("YES")
    else:
        print("NO")