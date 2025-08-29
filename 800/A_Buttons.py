t = int(input())
for i in range(t):
    a,b,c = list(map(int,input().split()))
    if c % 2 == 1:
        if b > a:
            print("Second")
        else:
            print("First")
    else:
        if a > b:
            print("First")
        else:
            print("Second")