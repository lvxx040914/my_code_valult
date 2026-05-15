import sys

def solve():
    # 使用快读提高效率
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    ptr = 0
    N = int(input_data[ptr]); ptr += 1
    V = int(input_data[ptr]); ptr += 1
    
    # dp[j] 表示容量为 j 时的最大价值
    dp = [0] * (V + 1)
    
    # 1. 遍历每一组
    for _ in range(N):
        S = int(input_data[ptr]); ptr += 1 # 当前组的物品数量
        items = []
        for _ in range(S):
            v = int(input_data[ptr]); ptr += 1
            w = int(input_data[ptr]); ptr += 1
            items.append((v, w))
            
        # 2. 逆序遍历容量 (确保 01 性质)
        for j in range(V, -1, -1):
            # 3. 遍历组内所有物品
            for v, w in items:
                if j >= v:
                    # 这里的 dp[j] 会在组内物品间竞争，最终只留下一件最值的
                    dp[j] = max(dp[j], dp[j - v] + w)
                    
    print(dp[V])

if __name__ == "__main__":
    solve()