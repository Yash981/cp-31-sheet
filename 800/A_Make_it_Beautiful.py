t = int(input())
for i in range(t):
    n = int(input())
    nums = list(map(int,input().split()))
    if nums[0] == nums[-1]:
        print("NO")
    else:
        print("YES")
        print(*([nums[-1]]+nums[0:-1]))