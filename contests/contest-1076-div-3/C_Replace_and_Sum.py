from itertools import accumulate


t = int(input())
for _ in range(t):
    n,q = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    arr = [max(a[i], b[i]) for i in range(n)]
    for i in range(n-2,-1,-1):
        if arr[i+1] > arr[i]:
            arr[i] = arr[i+1]
    pprefix = list(accumulate(arr))
    ans = []
    for _ in range(q):
        l,r = map(int, input().split())
        l -= 1
        r -= 1
        if l == 0:
            ans.append(pprefix[r])
        else:
            ans.append(pprefix[r] - pprefix[l-1])
    print(*ans)