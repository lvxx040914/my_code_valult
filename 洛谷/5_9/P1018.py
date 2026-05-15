n,k = map(int,input().split())
s = input().strip()
dp = [[0]*(k+1) for _ in range(n+1)]
#初始化
for i in range(1,n+1):
    dp[i][0] = int(s[:i])
#动态规划
for j in range(1,k+1):
    for i in range(j+1,n+1):
        for p in range(j,i):
            dp[i][j] = max(dp[i][j],dp[p][j-1]*int(s[p:i]))

print(dp[n][k])