import sys

def solve():
    input_data = sys.stdin.read().split()
    
    N,V = int(input_data[0]),int(input_data[1])
    dp = [0] * (V + 1)
    cur_idx = 2
    
    for _ in range(N):
        v = int(input_data[cur_idx])
        w = int(input_data[cur_idx + 1])
        s = int(input_data[cur_idx + 2])
        cur_idx += 3
        for _ in range(s):
            for i in range(V,v-1,-1):
                dp[i] = max(dp[i],dp[i-v]+w)
    print(dp[-1])

if __name__ == "__main__":
    solve()