for _ in range(int(input())):
    n = int(input())
    if n % 2 == 1 or n < 4:
        print(-1)
    else:
        min_buses = (n+5) // 6
        max_buses = n // 4
        print(min_buses,max_buses)

        
