N,V = map(int,input().split())
dp = [0]*(V+1)
for _ in range(N):
    v,w = map(int,input().split())
    for i in range(v,V+1):
        dp[i] = max(dp[i],dp[i-v]+w)
print(dp[-1])