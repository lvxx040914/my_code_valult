import sys
from bisect import bisect_left, bisect_right

data = sys.stdin.read().strip().split()
if not data:
    print(0)
    print(0)
else:
    a = list(map(int, data))

    # Longest non-increasing subsequence (LNIS)
    tails = []
    for x in a:
        y = -x
        i = bisect_right(tails, y)  # allow equal -> non-decreasing on -x
        if i == len(tails):
            tails.append(y)
        else:
            tails[i] = y
    lnis = len(tails)
    # Dilworth 定理
    # 最少划分成多少个不上升序列 = 最长严格上升子序列长度
    # Minimum number of non-increasing sequences to partition = length of LIS (strict)
    tails = []
    for x in a:
        i = bisect_left(tails, x)  # strict increasing
        if i == len(tails):
            tails.append(x)
        else:
            tails[i] = x
    min_sets = len(tails)

    print(lnis)
    print(min_sets)
