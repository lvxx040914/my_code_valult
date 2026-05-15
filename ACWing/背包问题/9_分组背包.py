import sys

def zero_one_pack(dp, v, m, w):
    for i in range(len(dp)-1, v-1, -1):
        for j in range(len(dp[i-v])-1, m-1, -1):
                dp[i][j] = max(dp[i][j], dp[i-v][j-m] + w)

def solve():
    input_data = sys.stdin.read().split()
    
    N,V,M = int(input_data[0]),int(input_data[1]),int(input_data[2])
    dp = [[0] * (M + 1) for _ in range(V + 1)]
    dp[0][0] = 0
    cur_idx = 3

    for _ in range(N):
        v = int(input_data[cur_idx])
        m = int(input_data[cur_idx + 1])
        w = int(input_data[cur_idx + 2])
        cur_idx += 3
        zero_one_pack(dp, v, m, w)
    print(dp[-1][-1])

if __name__ == "__main__":
    solve()