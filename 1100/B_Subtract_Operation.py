from collections import Counter
t = int(input())
for _ in range(t):
    n,k = map(int,input().split())
    arr = list(map(int,input().split()))
    freq = Counter(arr)
    for key,v in freq.items():
        if key-k in freq:
            print("YES")
            break
    else:
        print("NO")
