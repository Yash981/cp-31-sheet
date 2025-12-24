t = int(input())
for _ in range(t):
    n,r,b = map(int,input().split())
    quo = r // (b+1)
    rem = r % (b+1)
    distributeTimes = b+1
    res = []
    while distributeTimes:
        curr = []
        curr.append("R" * (quo))
        if rem:
            curr.append("R")
            rem -= 1
        res.append("".join(curr))
        distributeTimes -= 1
    print("B".join(res))


        
            