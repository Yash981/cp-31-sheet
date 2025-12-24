t = int(input())
def findingSubarrayAtleastGreaterThanOrEqK(n,k):
    if n < k:
         return 0
    return ((n-k+1) * (n-k+2)) // 2
for _ in range(t):
    n,k,q = map(int,input().split())
    arr = list(map(int,input().split()))
    curr = 0
    start = None
    ans = 0
    for x in range(n):
        if arr[x] <= q:
            if start == None:
                start = x
            curr += 1
        else:
            if start != None:
                    ans += findingSubarrayAtleastGreaterThanOrEqK(x-start,k)
            curr = 0
            start = None
    if start != None:
        ans += findingSubarrayAtleastGreaterThanOrEqK(n-start,k)
    print(ans)