import sys

# GitHub Copilot
# 题解：把字符串分成 k 份，计算每一段内可选单词起始位置的数量之和最大值
# 思路：预处理每个起始位置最早能匹配到的单词结束位置 min_end，
# 对于段 [t..j] 内，若 min_end[s] <= j 则起点 s 可被计入。用前缀和得到 val[t][j]。
# 动态规划 dp[i][r] 表示前 i 个字符分成 r 份的最大值（允许空段）。

data = [line.rstrip("\n") for line in sys.stdin]
ptr = 0
out_lines = []
INF = 10**9

while ptr < len(data):
    if not data[ptr].strip():
        ptr += 1
        continue
    parts = data[ptr].split()
    if not parts:
        ptr += 1
        continue
    p = int(parts[0]); k = int(parts[1])
    ptr += 1
    # 读取 p 行，每行正好 20 个字符
    s_lines = []
    for _ in range(p):
        s_lines.append(data[ptr])
        ptr += 1
    S = "".join(s_lines)
    n = len(S)
    # 读取字典
    s_cnt = int(data[ptr]); ptr += 1
    words = []
    for _ in range(s_cnt):
        words.append(data[ptr].strip())
        ptr += 1

    # 计算每个起点的最早结束位置（若无匹配则为 INF）
    min_end = [INF] * n
    for i in range(n):
        for w in words:
            L = len(w)
            if i + L <= n and S[i:i+L] == w:
                min_end[i] = min(min_end[i], i + L - 1)

    # 预计算 val[t][j]：区间 [t..j] 内可计数的起点数
    # 通过对每个 j 构造 good[i]=1(min_end[i] <= j) 的前缀和实现
    # 为节省内存只在需要时计算 val_row[j][t] 通过前缀和获取
    # 但为简单直接，构造 val 矩阵 O(n^2)
    val = [[0]*n for _ in range(n)]
    for j in range(n):
        pref = [0]*(n+1)
        for i in range(n):
            pref[i+1] = pref[i] + (1 if min_end[i] <= j else 0)
        for t in range(0, j+1):
            val[t][j] = pref[j+1] - pref[t]

    # dp[i][r] 前 i 字符分成 r 份的最大值（i from 0..n, r from 0..k）
    dp = [[-10**9]*(k+1) for _ in range(n+1)]
    # 空前缀分任意份均为 0（允许空段）
    for r in range(k+1):
        dp[0][r] = 0
    for i in range(1, n+1):
        dp[i][0] = -10**9  # 不能用 0 份覆盖非空前缀
    for i in range(1, n+1):
        for r in range(1, k+1):
            best = -10**9
            # t 从 0..i（允许最后一段为空，当 t==i 时段为空，值为 0）
            for t in range(0, i+1):
                add = 0
                if t <= i-1:
                    add = val[t][i-1]
                cand = dp[t][r-1] + add
                if cand > best:
                    best = cand
            dp[i][r] = best
    # 结果为前 n 字符分成 k 份的最大值
    res = dp[n][k]
    if res < 0:
        res = 0
    out_lines.append(str(res))

sys.stdout.write("\n".join(out_lines))