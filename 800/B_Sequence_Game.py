t = int(input())
for _ in range(t):
    n = int(input())
    nums = list(map(int,input().split()))
    ans = [nums[0]]
    for i in range(1,n):
        if nums[i] >= nums[i-1]:
            ans.append(nums[i])
        else:
            if nums[i]-1 < 1:
                ans.append(nums[i])
            else:
                ans.append(nums[i]-1)
            ans.append(nums[i])
    print(len(ans))
    print(*ans)
