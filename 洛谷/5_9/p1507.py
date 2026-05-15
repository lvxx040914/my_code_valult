import sys

input = sys.stdin.readline

H, T = map(int, input().split())

n = int(input())

dp = [[0] * (T + 1) for _ in range(H + 1)]

for _ in range(n):

    h, t, k = map(int, input().split())

    for i in range(H, h - 1, -1):

        dpi = dp[i]
        dpp = dp[i - h]

        for j in range(T, t - 1, -1):

            val = dpp[j - t] + k

            if val > dpi[j]:
                dpi[j] = val

print(dp[H][T])