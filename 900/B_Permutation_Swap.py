import math


t = int(input())
for _ in range(t):
    n = int(input())
    unsorted = list(map(int,input().split()))
    gcd = 0
    for i in range(n):
        gcd = math.gcd(gcd,abs(unsorted[i]-(i+1)))
    print(gcd)