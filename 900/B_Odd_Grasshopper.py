for _ in range(int(input())):
    x,n = map(int,input().split())
    quo,rem = divmod(n,4)
    currI = quo * 4
    while currI < n:
        currI += 1
        if x % 2 == 0:
            x -= currI
        else:
            x += currI
    print(x)