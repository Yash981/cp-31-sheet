t = int(input())
for _ in range(t):
    n = int(input())
    x = 1
    while n % x == 0:
        x += 1
    print(x-1)