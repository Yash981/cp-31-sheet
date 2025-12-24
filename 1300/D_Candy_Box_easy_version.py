from collections import Counter

t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int,input().split()))
    freq = list(Counter(arr).values())
    freq.sort(reverse=True)
    used = set()
    ans = 0
    for i,x in enumerate(freq):
        if x not in used:
            ans += x
            used.add(x)
        else:
            curr = x
            while curr > 0 and curr in used:
                curr -= 1
            if curr not in used:
                ans += curr
                used.add(curr)
    print(ans)