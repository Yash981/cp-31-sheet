from itertools import groupby
s = input()
n = len(s)
MOD = 10**9+7
ans = 1
splitB = s.split("b")
for i in splitB:
    if i == "":
        continue
    countA = i.count("a")
    ans *= (countA+1)
    ans %= MOD
print((ans-1)%MOD)
