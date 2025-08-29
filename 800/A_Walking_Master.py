t = int(input())
for _ in range(t):
    a,b,c,d = list(map(int,input().split()))
    """
    YunQian can go (x+1,y+1) to right up or can go (x-1,y) to left
                            x                           y
    right-up                +1                          +1
    left                    -1                           0
    X = a + R - L
    Y = b + R
    ---
    #y
    b + R = d
    d = b + R
    -R = b - d
    R = -b + d
    ---> R = d - b

    #x
    a + R - L = c
    c = a + R - L
    L = a + R - c
    L = a + (d-b) - c

    answer 
    if R < 0 or L < 0 return -1
    else L + R(minMoves)
    """
    R = d - b
    L = a + (d-b) - c
    if R < 0 or L < 0:
        print(-1)
    else:
        print(R+L)



