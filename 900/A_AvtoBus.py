import math
for _ in range(int(input())):
    n = int(input())
    if n % 2 == 1 or n < 4:
        print(-1)
    else:
        min_buses = n // 6
        remainder = n % 6

        if remainder == 0:
            print(min_buses, n // 4)
        elif remainder == 4:
            print(min_buses + 1, n // 4)
        else:
            print(-1)
