t = int(input())
for _ in range(t):
    n,k,x = map(int,input().split())
    #key point here is for 1 to 5 total will be 15 , you can always make by distinct nums(1 to 5) from value (1 to 15) so we need to check x in range of  min sum and maxsum
    minSum = k * (k+1)//2
    # print(minSum)
    maxSum = (n * (n+1)//2) - ((n-k) * (n-k+1)//2)
    # print(maxSum)
    if minSum <= x <= maxSum:
        print("YES")
    else:
        print("NO")