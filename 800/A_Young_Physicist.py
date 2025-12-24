n = int(input())
ans = [0,0,0]
for _ in range(n):
    a,b,c = map(int,input().split())
    ans[0] += a
    ans[1] += b
    ans[2] += c
    
print("YES" if ans[0]==ans[1]==ans[2]==0 else "NO")