from collections import Counter
t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    ht = Counter()
    for i in arr:
        ht[i.bit_length()] += 1
    ans = 0
    for key,val in ht.items():
        ans += val * (val - 1) // 2
    print(ans)