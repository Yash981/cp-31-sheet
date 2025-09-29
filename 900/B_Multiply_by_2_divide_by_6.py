for _ in range(int(input())):
    n = int(input())
    def count_prime_factor(n, p):
        count = 0
        while n % p == 0 and n >= 1:
            count += 1
            n //= p
        return [n,count]
    
    val,res3 = count_prime_factor(n,3)
    val2,res2 = count_prime_factor(val,2)
    if val2 > 1 or res2 > res3:
        print(-1)
    else:
        print(res3+(res3-res2)) # because 6 = 2 x 3 so we are taking all 3's and remaining res3-res2 will be multiply by 2 


"""
Why this formula works

res3 = number of 3s in n

Each divide by 6 removes 1 factor of 3 and 1 factor of 2.

So to remove all 3s, you need to do res3 divides by 6.

res2 = number of 2s in n

But each divide by 6 also removes 1 factor of 2.

If you have fewer 2s than 3s (res2 < res3), you need to multiply by 2 to “add more 2s” before dividing by 6.

How many multiplications? → (res3 - res2)

Total moves

res3 → divides by 6

res3 - res2 → multiplies by 2 to balance powers

Total = res3 + (res3 - res2) = 2*res3 - res2
"""