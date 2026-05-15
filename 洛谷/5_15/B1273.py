n,V = map(int, input().split())
dp = [0]* (V+1)

for _ in range(n):
    w,v,c = map(int, input().split())
    for i in range(c):
        for j in range(V,w-1,-1):
            dp[j] = max(dp[j],dp[j-w]+v)
print(dp[V])