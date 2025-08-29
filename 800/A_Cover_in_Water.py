t = int(input())
for i in range(t):
    n = int(input())
    s = input()
    l = []
    count = 0
    for j in range(n):
        if s[j] =='.':
            count += 1
        else:
            l.append(count)
            count = 0
    l.append(count)
    
    for k in l:
        if k >= 3:
            print(2)
            break
    else:
        print(sum(l))

