import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int,input().split()))
    mx = max(arr)
    limit = 2 * mx
    squares = []
    i = 0
    while i * i < limit:
        squares.append(i * i)
        i += 1
    total = (n * (n+1))//2
    prefixXor = 0
    freq = [0] * limit
    freq[0] = 1
    oddSubbarrays = 0
    for v in arr:
        prefixXor ^= v
        x = 0
        while x * x < limit:
            if ((prefixXor^(x*x)) < limit):
                oddSubbarrays += freq[prefixXor^(x*x)]
            else:
                break
            x += 1
        freq[prefixXor] += 1
    print(total-oddSubbarrays)