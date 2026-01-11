n,m = map(int,input().split())
arr = list(map(int,input().split()))
arr.sort()
print(abs(arr[0]-arr[-1]) % m)