s = input()
n = len(s)
prefix = [0] * (n + 1)

for i in range(1, n):
    prefix[i + 1] = prefix[i]
    if s[i] == 'v' and s[i - 1] == 'v':
        prefix[i + 1] += 1

suffix = [0] * (n + 1)

for i in range(n - 2, -1, -1):
    suffix[i] = suffix[i + 1]
    if s[i] == 'v' and s[i + 1] == 'v':
        suffix[i] += 1
ans = 0
for i in range(n):
    if s[i] == 'o':
        ans += prefix[i] * suffix[i]

print(ans)
    