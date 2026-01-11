from collections import Counter,defaultdict
from itertools import groupby
t = int(input())
def countNumberOfSubarrays(a,b):
    n = len(a)
    i = 0
    j = 0
    notEqual = [0] * n
    res = 0
    while i < n and j < n:
        if a[i] != b[j]:
            notEqual[i] = 1
        i += 1
        j += 1
    for key,group in groupby(notEqual):
        if key == 0:
            groupLength = len(list(group))
            res += (groupLength*(groupLength+1))//2
    return res
for _ in range(t):
    n,k = map(int,input().split())
    a = [x for x in input()]
    b = [x for x in input()]
    initialFreq = Counter(a)
    subarrayFreq = defaultdict(list)
    for index,(key,grp) in enumerate(groupby(a)):
        length = len(list(grp))
        if length > 1:
            subarrayFreq[key].append((index,index+length-1))
    i = 0
    j = 0
    ans = countNumberOfSubarrays(a,b)
    print("before",ans)
    currFreq = Counter()
    unique = 0
    while j < n:
        currFreq[a[j]] += 1
        if currFreq[a[j]] == 1:
            unique += 1
        while unique > k:
            currFreq[a[i]] -= 1
            if currFreq[a[i]] == 0:
                unique -= 1
            i += 1
        length = j-i+1
        res = length * (length+1)//2
        for key,val in currFreq.items():
            rem = initialFreq[key] - val
            remSub = rem - sum([x[1]-x[0]+1 for x in subarrayFreq[key] if not (x[0] >= i and x[1] <= j)])
            res += remSub
            #TODO: here i have to add each subarrayFreq[key] as (n*(n+1))//2 but that subarrayFreq[key] may contain subarray of currOne so i have to remove that
            for x in subarrayFreq[key]:
                if not (x[0] >= i and x[1] <= j):
                    res += (x[1]-x[0]+1)*(x[1]-x[0]+2)//2
        ans = max(ans,res)
        j += 1
    print(ans)


    
    