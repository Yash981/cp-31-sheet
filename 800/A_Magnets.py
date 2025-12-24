n = int(input())
prev = ""
ans = 0
for _ in range(n):
    s = input()
    if s == prev:
        continue
    ans += 1
    prev = s
print(ans)