t = int(input())
for _ in range(t):
    n = int(input())
    if n % 2 == 0:
        if (n // 2) > 1:
            if n > 0 and (n & (n - 1)) == 0: #condition to check is N is power of 2 
                print("NO")
            else:
                print("YES")
        else:
            print("NO")
    else:
        print("YES")