t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int,input().split()))
    if n % 2 == 0:
        print(2)
        print(1,n)
        print(1,n)
    else:
        """
        Small dry run (n = 3) — array [9, 9, 9]
Do [1,2]: s=9^9=0
s=9^9=0 → after first op [0,0,9].

Do [1,2] again: segment XOR = 0^0=0
0^0=0 → still [0,0,9] (they are already zeros).

Do [2,3]: s=0^9=9
s=0^9=9 → after op [0,9,9].

Do [2,3] again: s=9^9=0
s=9^9=0 → after op [0,0,0].
        """
        print(4)
        print(1,n)
        print(1,2)
        print(2,n)
        print(2,n)