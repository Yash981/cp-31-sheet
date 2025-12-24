t = int(input())
for _ in range(t):
    x,y,k = map(int,input().split())
    target = k + (y*k)
    curr = 1
    while curr < target:
        print("op",curr)
        curr -= 1
        curr += x
    print(curr)
    """
    9
    370-312 = 58
    """