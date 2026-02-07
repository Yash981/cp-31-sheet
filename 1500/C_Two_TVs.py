n = int(input())
arr = []
for _ in range(n):
    l,r = map(int,input().split())
    arr.append([l,1])
    arr.append([r+1,-1])
arr.sort()
curr = 0
for i in range(len(arr)):
    curr += arr[i][1]
    if curr > 2:
        print("NO")
        exit()
print("YES")