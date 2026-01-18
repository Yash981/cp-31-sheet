t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    if any(x % 10 in (0,5) for x in arr):
        newarr = [x + (x % 10) for x in arr]  # 5 → 10
        if len(set(newarr)) == 1:
            print("Yes")
        else:
            print("No")
        continue
    mods = set()
    for i,x in enumerate(arr):
        while x % 10 != 2:
            x += x % 10
        mods.add(x % 20)
    print("Yes" if len(mods) == 1 else "No")