t = int(input())
for i in range(t):
    n, x = list(map(int,input().split()))
    nums = list(map(int,input().split()))
    prev = 0
    ans = 0
    for i in range(n):
        ans = max(ans,nums[i]-prev)
        prev = nums[i]
    print(max(ans,2*(x-prev)))
