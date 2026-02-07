t = int(input())
for _ in range(t):
    n = int(input())
    """
    till first 0 count trailing 1s from right side + first 0
    00000 - 0


    00001 - 1
    00010 - 2
    00011 - 1
    00100 - 3
    00101 - 1
    00110 - 2
    00111 - 1
    01000 - 4

    01001 - 1
    01010 - 2
    01011 - 1
    01100 - 3
    01101 - 1
    01110 - 2
    01111 - 1
    10000 - 5
    """
    print(2*n - n.bit_count())

    