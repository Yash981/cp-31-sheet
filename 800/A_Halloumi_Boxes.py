t = int(input())
for i in range(t):
    n,k = list(map(int,input().split()))
    nums = list(map(int,input().split()))
    sortedNums = sorted(nums)
    if k == 1 and nums[:] == sortedNums:
        print("YES")
    elif k == 1 and nums[:] != sortedNums:
        print("NO")
    else:
        print("YES")
