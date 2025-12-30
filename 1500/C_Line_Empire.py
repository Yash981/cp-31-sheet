t = int(input())
for _ in range(t):
    n,a,b = map(int,input().split())
    posy = list(map(int,input().split()))
    #opt:1 -> move ahead to the conquered kingdom and do a * abs(currPos - futurePos)
    #opt:2 -> move ahead  to the unconquered kingdom and do b * abs(currPos - futurePos)
    