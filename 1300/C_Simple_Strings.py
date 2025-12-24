s = input()
s = [x for x in s]
n = len(s)
for i in range(1,n):
    if s[i] == s[i-1]:
        prev = s[i-1]
        if i+1 < n:
            nextt = s[i+1]
            for j in range(26):
                if chr(j+97) != prev and chr(j+97) != nextt:
                    s[i] = chr(j+97)
                    break
        else:
            for j in range(26):
                if chr(j+97) != prev:
                    s[i] = chr(j+97)
                    break
print("".join(s))
