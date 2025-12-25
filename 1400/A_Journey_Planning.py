from collections import Counter
n = int(input())
arr = list(map(int,input().split()))
modified = [(arr[i],i-arr[i]) for i in range(n)]
freq = Counter()
for i,x in enumerate(modified):
    freq[x[1]] += x[0]
print(max(freq.values()))
