t = int(input())
for _ in range(t):
    k,x = map(int,input().split())
    if k >= x:
        print((x*(x+1))//2)
    else:
        l = 1
        r = k
        currAns = 0
        while l <= r:
            mid = l + (r-l)//2
            if (mid * (mid+1))//2 < x:
                currAns = mid
                l = mid + 1
            else:
                r = mid - 1
        if (currAns * (currAns+1))//2 < x and currAns+1 <= k:
            currAns += 1
        if (currAns * (currAns+1))//2 >= x:
            print(currAns)
        else:
            x -= (currAns * (currAns+1))//2
            print("here",currAns,x)
            start = k-1
            l = 1
            r = k-1
            res = 0
            while l <= r:
                mid = l + (r-l)//2
                if (start*(start+1))//2 - max(0,((mid-1)*((mid-1)+1))//2) >= x:
                    res = start-mid
                    r = mid - 1
                else:
                    l = mid + 1
            print(currAns+res)
    