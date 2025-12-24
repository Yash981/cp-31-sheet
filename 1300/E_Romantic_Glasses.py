# import sys
# input = sys.stdin.readline
# t = int(input())
# for _ in range(t):
#     n = int(input())
#     arr = list(map(int,input().split()))
#     seen = set()
#     curr = 0
#     flag = 1
#     found = False
#     for i in range(n):
#         if flag==1:
#             curr += arr[i]
#             flag = 0
#         else:
#             curr -= arr[i]
#             flag= 1
#         if curr == 0 or curr in seen:
#             found = True
#             break
#         seen.add(curr)
#     print("YES" if found else "NO")

for i in range(1,10**9):
    print(i)