n = int(input())
total = n*(n+1)//2
arr = list(map(int,input().split()))
parity = [0]
for i in arr:
    if i < 0:
        parity.append(1)
    else:
        parity.append(0)
prefixParity = [0]
for i in range(1,len(parity)):
    prefixParity.append((prefixParity[-1]+parity[i]) % 2)
zeroes = prefixParity.count(0)
one = prefixParity.count(1)
#positive product = math.comb(zeroes,2)+math.comb(one,2)
#negative product = zeroes*one
#total subarrays = n*(n+1)//2
print(zeroes*one,total-(zeroes*one))