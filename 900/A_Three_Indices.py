t = int(input())
for _ in range(t):
    def f():
        n = int(input())
        arr = list(map(int,input().split()))
        def prefixFn(nums,reversIndex):
            prefix = []
            for i,x in enumerate(nums,1):
                if not prefix:
                    if reversIndex:
                        prefix.append([x,reversIndex-i+1])
                    else:
                        prefix.append([x,i])
                else:
                    if prefix[-1][0] < x:
                        prefix.append(prefix[-1])
                    else:
                        if reversIndex:
                            prefix.append([x,reversIndex-i+1])
                        else:
                            prefix.append([x,i])
            return prefix
        pref = prefixFn(arr,None)
        suff = prefixFn(arr[::-1],n)[::-1]
        for i,x in enumerate(arr[1:n-1],1):
            if pref[i-1][0] < x and x > suff[i+1][0]:
                print("YES")
                print(pref[i-1][1],i+1,suff[i+1][1])
                return
        print("NO")
        return
    f()

