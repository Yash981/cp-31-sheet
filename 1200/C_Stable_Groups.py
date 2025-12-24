n,k,x = map(int,input().split())
arr = list(map(int,input().split()))
arr.sort()
gaps = []
for i in range(n):
    diff = arr[i]-arr[i-1]
    if diff > x:
        gaps.append(diff)
gaps.sort()
for i in range(len(gaps)):
    segments = (gaps[i]-1)//x
    if k >= segments:
        k -= segments
    else:
        print(len(gaps)-i+1)
        break
else:
    print(1)
