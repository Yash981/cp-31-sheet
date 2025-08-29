n = int(input())
nums = list(map(int,input().split()))
newNums = []
for i in range(n):
    newNums.append(abs(nums[i]-0))
newNums.sort()
print(newNums[0])
