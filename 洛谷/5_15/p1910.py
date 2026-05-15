n,m,x = map(int, input().split())
dp = [[0]*(x+1) for _ in range(m+1)]

for _ in range(n):
    a,b,c = map(int, input().split())
    for j in range(m, b-1,-1):
        for k in range(x, c-1,-1):
            dp[j][k] = max(dp[j][k], dp[j-b][k-c]+a)
print(dp[m][x])