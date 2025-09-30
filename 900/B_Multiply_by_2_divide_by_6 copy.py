t = int(input())
for i in range(t):
    n = int(input())
    operations = 0
    while n > 1:
        if n%6 ==0:
            n //= 6
        elif n%2 == 0:
            n *= 2
        else:
            print(-1)
            break
        operations += 1
    print(operations)