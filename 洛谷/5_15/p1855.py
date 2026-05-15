import sys

def solve():
    input_data = sys.stdin.read().split()
    n,M,T = int(input_data[0]), int(input_data[1]), int(input_data[2])
    ptr = 3
    dp = [[0]*(T+1) for _ in range(M+1)]

    for i in range(n):
        m,t = int(input_data[ptr]), int(input_data[ptr+1])
        ptr += 2
        for j in range(M,m-1,-1):
            for k in range(T,t-1,-1):
                dp[j][k] = max(dp[j][k], dp[j-m][k-t]+1)
    print(dp[M][T])

if __name__ == "__main__":
    solve()