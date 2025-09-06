t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    ans = 0
    curr = 0
    prev = None
    for i in range(n):
        if prev==None or prev == s[i]:
            prev = s[i]
            curr += 1
        else:
            ans = max(ans,curr+1)
            prev = s[i]
            curr = 1
    ans = max(ans,curr+1)
    print(ans)
        