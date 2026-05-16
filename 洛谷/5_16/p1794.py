import sys

V,G = map(int,input().split())
N = int(input())
input_data = sys.stdin.read().split()
dp = [[0]*(G+1) for _ in range(V+1)]
idx = 0
for _ in range(N):
    t,v,g = int(input_data[idx]),int(input_data[idx+1]),int(input_data[idx+2])
    idx += 3
    for i in range(V,v-1,-1):
        for j in range(G,g-1,-1):
            dp[i][j] = max(dp[i][j],dp[i-v][j-g]+t)
print(dp[V][G])

