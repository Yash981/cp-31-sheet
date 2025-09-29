t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int,input().split()))
    ones = arr.count(1)
    zeroes = arr.count(0)
    subzeroes = pow(2,zeroes)-1
    print(ones+ones*subzeroes)
