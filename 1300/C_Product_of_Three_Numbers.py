t = int(input())
for _ in range(t):
    n = int(input())
    curr = 2
    a = None
    b = None
    while curr < 1000 and (a == None or b == None):
        if n % curr == 0:
            if a == None:
                a = curr
            else:
                b = curr
        curr += 1
    if a!=None and b != None and n % (a*b) == 0 and a!=(n//(a*b)) and b!=(n//(a*b)) and a!=b and a>1 and b>1 and (n//(a*b)) > 1:
        print("YES")
        print(a,b,n//(a*b))
    else:
        print("NO")