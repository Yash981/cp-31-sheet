t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int,input().split()))

    queries = []
    for _ in range(int((input()))):
        l,r = map(int,input().split())
        queries.append([l,r])
    nextDiff = [-1] * n
    for i in range(n-2,-1,-1):
        if arr[i] == arr[i+1]:
            nextDiff[i] = nextDiff[i+1]
        else:
            nextDiff[i] = i+1
    # print(nextDiff)
    for l,r in queries:
        l -= 1
        r -= 1
        if nextDiff[l] != -1 and nextDiff[l] <= r:
            print(l+1,nextDiff[l]+1)
        else:
            print(-1,-1)
