from collections import defaultdict,Counter


t = int(input())
for _ in range(t):
    s = input()
    freq = Counter(s)
    if len(freq) == 1:
        print("YES")
        continue
    if len(freq) == 2:
        for x in range(len(s)-1):
            if s[x] == s[x+1]:
                print("NO")
                break
        else:
            print("YES")
    else:
        i = 0
        j = 0
        ht = Counter()
        count = 0
        while j < len(s):
            ht[s[j]] += 1
            if ht[s[j]] == 1:
                count += 1
            while count > 2:
                ht[s[i]] -= 1
                if ht[s[i]] == 0: 
                    count -= 1
                i += 1
            if count == 2:
                values = set(freq.values())
                flag = False
                for val in values:
                    if val > 1:
                        flag = True
                        print("NO")
                        break
                if flag:
                    break
            j += 1
        else:
            print("YES")



