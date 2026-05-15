n,m = map(int,input().split())
dp = [[0]*n for _ in range(m+1)]
dp[0][0] = 1
for k in range(1,m+1):
    for i in range(n):
        dp[k][i] = dp[k-1][(i-1+n)%n]+dp[k-1][(i+1)%n]
print(dp[m][0])