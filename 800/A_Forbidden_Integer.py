# from functools import lru_cache
# t = int(input())
# for i in range(t):
#     n,k,skip = list(map(int,input().split()))
#     @lru_cache(None)
#     def f(total,steps):
#         if total > n:
#             return 1e9,()
#         if total == n:
#             return 0,steps
#         res = 1e9
#         best = ()
#         for x in range(1,k+1):
#             if x != skip:
#                 current_res, current_steps = f(total + x, steps+(x,))
#                 if current_res + 1 < res:
#                     res = current_res + 1
#                     best = current_steps
#         return res,best
#     ans = f(0,())
#     f.cache_clear()
#     if ans[0] >= 1e9:
#         print('NO')
#     else:
#         print('YES')
#         print(ans[0])
#         print(*ans[1])

t = int(input())
for _ in range(t):
    n, k, skip = list(map(int, input().split()))
    if skip != 1:
        print('YES')
        print(*[[1]*n])
    if k == 1 or (k==2 and n%2 == 1):
        print('NO')
    else:
        print('YES')
        

        
        