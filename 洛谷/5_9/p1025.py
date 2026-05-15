# 计算将整数 n 分成 k 份（每份至少为 1），且不考虑顺序的不同分法数
# 输入：整数 n, k（假定 n,k 为正整数）
# 返回：不同分法的数量（整数）
def count_partitions(n: int, k: int) -> int:
    # dp[i][j] 表示将整数 i 分成 j 份（每份至少为1，不考虑顺序）的方案数
    dp = [[0] * (k + 1) for _ in range(n + 1)]
    dp[0][0] = 1  # 将0分成0份有1种空方案

    # 根据递推：p_k(n) = p_{k-1}(n-1) + p_k(n-k)
    for i in range(1, n + 1):
        for j in range(1, k + 1):
            # 把一个 1 放到某一份：等价于把 i-1 分成 j-1 份
            a = dp[i - 1][j - 1] if i - 1 >= 0 else 0
            # 每份至少再减去1（即所有份都至少为2）：等价于把 i-j 分成 j 份
            b = dp[i - j][j] if i - j >= 0 else 0
            dp[i][j] = a + b

    return dp[n][k]
n,k = map(int, input().split())
print(count_partitions(n, k))

#problem 2
# from functools import lru_cache

# n, k = map(int, input().split())

# @lru_cache(None)
# def dfs(remain, cnt, start):
#     # 正好分完
#     if remain == 0 and cnt == 0:
#         return 1

#     # 非法情况
#     if remain < 0 or cnt == 0:
#         return 0

#     ans = 0

#     # 枚举当前这一份
#     for x in range(start, remain + 1):
#         ans += dfs(remain - x, cnt - 1, x)

#     return ans

# print(dfs(n, k, 1))