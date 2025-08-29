t = int(input())
for i in range(t):
    n,m = list(map(int,input().split()))
    nX = input()
    mS = input()
    operations = 0
    times = 6
    i = 0
    while i < times:
        if mS in nX:
            print(operations)
            break
        nX += nX
        operations += 1
        i += 1
    if i == times:
        print(-1)