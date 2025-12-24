n,k = map(int,input().split())
arr = list(map(int,input().split()))

i = 0
j = 0
currSum = 0
ans = 0
while j < n:
    currSum += arr[j]
    if j-i+1 < k:
        j += 1
    else:
        ans += currSum
        currSum -= arr[i]
        i += 1
        j += 1
print(f"{ans/(n-k+1):.10f}")