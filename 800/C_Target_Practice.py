t = int(input())
for i in range(t):
    values = [1,1,1,1,1,1,1,1,1,1],[1,2,2,2,2,2,2,2,2,1],[1,2,3,3,3,3,3,3,2,1],[1,2,3,4,4,4,4,3,2,1],[1,2,3,4,5,5,4,3,2,1],[1,2,3,4,5,5,4,3,2,1],[1,2,3,4,4,4,4,3,2,1],[1,2,3,3,3,3,3,3,2,1],[1,2,2,2,2,2,2,2,2,1],[1,1,1,1,1,1,1,1,1,1]
    xValues = []
    for x in range(10):
        line = input()
        s = []
        for y in line:
            s.append(y)
        xValues.append(s)
    ans = 0
    for a in range(10):
        for b in range(10):
            if xValues[a][b] == 'X':
                ans += values[a][b]
    print(ans)           


        



