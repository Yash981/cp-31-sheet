t = int(input())
for _ in range(t):
    a,b,c = map(int,input().split())
    newA = 2*b - c
    newB = (a+c)//2
    newC = 2*b - a
    if (newA > 0 and newA % a == 0) or (newB > 0 and newB % b == 0 and (c - a) % 2 == 0) or (newC > 0 and newC % c == 0):
        print("YES")
    else:
        print("NO")