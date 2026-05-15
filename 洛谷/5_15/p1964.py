import sys
from collections import defaultdict

def main():
    input = sys.stdin.read().splitlines()
    idx = 0
    m, n = map(int, input[idx].split())
    idx += 1
    
    # 第一步：合并同名物品
    item_dict = defaultdict(lambda: [0, 0, 0])  # [总数量, 总价值, 单格容量]
    for _ in range(n):
        parts = input[idx].split()
        idx += 1
        a = int(parts[0])
        b = int(parts[1])
        c = int(parts[2])
        st = parts[3]
        # 合并：数量累加，价值是单件价值，单格容量相同
        item_dict[st][0] += a
        item_dict[st][1] = b  # 同名物品单件价值相同
        item_dict[st][2] = c
    
    # 第二步：处理物品，计算每种物品最多需要多少格，以及每格的价值
    items = []
    total_space = 21 - m  # 背包可用容量
    if total_space <= 0:
        print(0)
        return
    
    for name, (a, b, c) in item_dict.items():
        if a == 0 or b == 0:
            continue  # 无价值/无数量，跳过
        # 计算该物品最多需要多少格
        max_cnt = (a + c - 1) // c  # 向上取整
        # 每一格的价值 = 单格放的数量 * 单件价值
        val_per = c * b
        items.append((max_cnt, val_per))
    
    # 第三步：多重背包 二进制优化
    dp = [0] * (total_space + 1)
    for max_cnt, val in items:
        # 二进制拆分
        k = 1
        rest = max_cnt
        while rest > 0:
            num = min(k, rest)
            # 01背包
            for j in range(total_space, num - 1, -1):
                if dp[j - num] + num * val > dp[j]:
                    dp[j] = dp[j - num] + num * val
            rest -= num
            k <<= 1
    
    print(max(dp))

if __name__ == "__main__":
    main()