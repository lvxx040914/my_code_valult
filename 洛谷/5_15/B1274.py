n,V = map(int, input().split())
dp = [0]* (V+1)

for _ in range(n):
    w,v = map(int, input().split())
    for j in range(w,V+1):
        dp[j] = max(dp[j], dp[j-w]+v)
print(dp[V])