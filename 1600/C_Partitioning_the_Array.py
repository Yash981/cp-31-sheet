import math
t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    factors = []
    for i in range(1,math.isqrt(n)+1):
        if n % i == 0:
            factors.append(i)
            if i != n // i:
                factors.append(n // i)
    factors.sort()
    ans = 0
    for i in factors:
        gcdd = 0
        for curr in range(i):
            for j in range(curr,n,i):
                gcdd = math.gcd(gcdd,arr[j]-arr[curr])
        if gcdd != 1:
            ans += 1
    print(ans)
        
    

            
    
    