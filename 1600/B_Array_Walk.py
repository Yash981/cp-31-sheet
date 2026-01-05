from itertools import accumulate
t = int(input())
for _ in range(t):
    n,k,z = map(int,input().split())
    arr = list(map(int,input().split()))
    prefix = [0] + list(accumulate(arr))
    best_pair = []
    best_pair.append(arr[0]+arr[1])
    for i in range(1,n-1):
        best_pair.append(max(best_pair[-1],arr[i]+arr[i+1]))
    zUsage = 0
    ans = 0
    while zUsage <= z and 2*zUsage <= k:
        RightMoves = k - 2*zUsage
        leftMoves = prefix[RightMoves+1]
        limit  = min(RightMoves,n-2)
        bouncingPairs = best_pair[limit]
        ans = max(ans,leftMoves+(zUsage) * bouncingPairs)
        zUsage += 1
    print(ans)

        

        
        
