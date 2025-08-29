from collections import Counter
t = int(input())
for _ in range(t):
    n = int(input())
    nums = list(map(int,input().split()))
    if n <= 2:
        print("Yes")
        continue
    else:
        if len(set(nums)) == 1:
            print("Yes")
            continue
        hashtable = Counter(nums)
        for i,j in hashtable.items():
            if j == n//2 and len(hashtable) == 2:
                print("Yes")
                break
        else:
            print("No")
