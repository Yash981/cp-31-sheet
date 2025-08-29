from math import ceil


t = int(input())
for _ in range(t):
    n = int(input())
    nums = list(map(int,input().split()))
    countOne = nums.count(1)
    countMinusOne = nums.count(-1)

    if countOne >= countMinusOne:
        if countMinusOne % 2 == 0:
            print(0)
        else:
            print(1)
    else:
        half = ceil(n/2)
        rem = half - countOne
        if (countMinusOne - rem) % 2 == 0:
            print(rem)
        elif (countMinusOne-rem) % 2 == 1:
            print(rem+1)