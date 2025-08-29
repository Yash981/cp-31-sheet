t = int(input())
for _ in range(t):
    x,k = list(map(int,input().split()))
    if x%k != 0:
        print(1)
        print(x)
    else:
        print(2)
        print(*[1,x-1])
