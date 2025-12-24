n,t = map(int,input().split())
s = [x for x in input()]
while t:
    i = 0
    while i < n:
        if i + 1 < n and s[i] == "B" and s[i+1] == "G":
            s[i],s[i+1] = s[i+1],s[i]
            i += 2
        else:
            i += 1
    t -= 1
print("".join(s))