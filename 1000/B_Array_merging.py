from itertools import groupby
t = int(input())
for _ in range(t):
    n = int(input())
    arr1 = list(map(int,input().split()))
    arr2 = list(map(int,input().split()))
    ans = 0
    def findLength(arr):
        res = 0
        for k,g in groupby(arr):
            res = max(res,len(list(g)))
        return res
    ans = max(ans,findLength(arr1),findLength(arr2),findLength(arr1+arr2[::-1]),findLength(arr1+arr2),findLength(arr2[::-1]+arr1),findLength(arr2+arr1))
    print(ans)
