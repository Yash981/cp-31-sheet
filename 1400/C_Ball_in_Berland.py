from collections import Counter
import math
t = int(input())
for _ in range(t):
    a,b,k = map(int, input().split())
    arr1 = list(map(int, input().split()))
    arr2 = list(map(int, input().split()))
    freq1 = Counter()
    freq2 = Counter()
    for i in range(len(arr1)):
        freq1[arr1[i]] += 1
        freq2[arr2[i]] += 1
    
    totalpairs = math.comb(k, 2)
    for key,value in freq1.items():
        totalpairs -= math.comb(value, 2)
    for key,value in freq2.items():
        totalpairs -= math.comb(value, 2)
    print(totalpairs)
    