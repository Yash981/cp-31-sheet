t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int,input().split()))
    if n == 1: print(0);continue
    print(max(max(arr[1:]) - arr[0],arr[-1] - min(arr[:-1]),max(arr[i] - arr[(i+1) % n] for i in range(n))))
    """
    1 8 1 2
    8 1 2 1
    1 2 1 8
    """