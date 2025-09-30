from collections import Counter
t = int(input())
for x in range(t):
    n,k = list(map(int,input().split()))
    s = input()
    freq = Counter(s)
    freqOdd = Counter()
    for key,v in freq.items():
        if v % 2 == 1:
            freqOdd[key] += v
    # print(freqOdd)
    newOddFreq = Counter()
    for key2,v2 in freqOdd.items():
        if k >= 1 and v2 >= 1:
            if v2 - 1 == 0:
                k -= 1
                continue
            newOddFreq[key2] = v2 - 1
            k -= 1
        else:
            newOddFreq[key2] = v2
    # print(newOddFreq)
    oddCount = 0
    for key3,v3 in newOddFreq.items():
        if v3 % 2 == 1:
            oddCount += 1
    if oddCount <= 1:
        print("YES")
    else:
        print("NO")
    
            




    
    
