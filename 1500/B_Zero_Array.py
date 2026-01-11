n = int(input())
arr = list(map(int, input().split()))
total = sum(arr)
mx = max(arr)
if total % 2 == 0:
    if mx <= total // 2:
        print("YES")
    else:
        print("NO")
else:
    print("NO")