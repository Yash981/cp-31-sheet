import math
t = int(input())
for _ in range(t):
    n,x = map(int,input().split())
    arr = list(map(int,input().split()))
    mx = sum(math.ceil(i/x)for i in arr)
    mn = math.ceil(sum(arr)/x)
    print(mn,mx)