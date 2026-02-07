t = int(input())
for _ in range(t):
    n,x,y = map(int,input().split())
    arr = list(map(int,input().split()))
    alice = x
    bob = x + 3
    target = y
    def dp(i,target,start):
        if target == 0:
            return True
        if target < 0:
            return False
        if i >= n:
            return target==0
        ans = False
        ans |= dp(i+1,target-(start+arr[i]),start)
        ans |= dp(i+1,target-(start^arr[i]),start)
        return ans
    a = dp(0,target,alice)
    b = dp(0,target,bob)
    print(a,b)