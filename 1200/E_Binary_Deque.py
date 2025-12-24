t = int(input())
for _ in range(t):
    n,k = map(int,input().split())
    arr = list(map(int,input().split()))
    total = sum(arr)
    if total < k:
        print(-1)
    else:
        i = 0
        j = 0
        currSum = 0
        ans = 0
        while j < n:
            currSum += arr[j]
            while currSum > k:
                currSum -= arr[i]
                i += 1
            ans = max(ans,j-i+1)
            j += 1
        print(n-ans)
            


