t = int(input())
for _ in range(t):
    n = int(input())
    arr = [x for x in input()]
    posy = []
    for i in range(n):
        if arr[i] == "*":
            posy.append(i)
    median = []
    for i in range(len(posy)):
        median.append(posy[i]-i)
    length = len(median)
    if not median:
        print(0)
        continue
    mid = median[length//2]
    start = mid
    idx = 0
    ans = 0
    while start < n and idx < len(posy):
        ans += abs(posy[idx]-start)
        idx += 1
        start += 1
    print(ans)