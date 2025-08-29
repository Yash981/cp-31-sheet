from collections import Counter
t = int(input())
for _ in range(t):
    n = int(input())
    nums = list(map(int,input().split()))
    if len(set(nums)) == 1:
        print(-1)
        continue
    ans1 = []
    ans2 = []
    freq = Counter(nums)
    val = max(nums)
    ans2.extend([val]*freq[val])
    for i in range(n):
        if nums[i] != val:
            ans1.append(nums[i])
    if ans1 and ans2:
        print(len(ans1),len(ans2))
        print(*ans1)
        print(*ans2)
    else:
        print(-1)
    

    


