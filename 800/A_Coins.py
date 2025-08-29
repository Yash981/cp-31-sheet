t = int(input())
for i in range(t):
    n,k = list(map(int,input().split()))
    val = n - k 
    if n%2 == 0 or val % 2 == 0:
        print("YES")
    else:
        print("NO")