import sys

def solve():
    input_data = sys.stdin.read().split()
    
    ptr = 0
    N = int(input_data[ptr]); ptr += 1
    V = int(input_data[ptr]); ptr += 1
    
    v = [0] * (N + 1)
    w = [0] * (N + 1)
    for i in range(1, N + 1):
        v[i] = int(input_data[ptr]); ptr += 1
        w[i] = int(input_data[ptr]); ptr += 1
        
    # f[i][j] 表示从第 i 个物品到最后一个物品中选，容量为 j 时的最大价值
    f = [[0] * (V + 1) for _ in range(N + 2)]
    
    # 1. 逆向 DP
    for i in range(N, 0, -1):
        for j in range(V + 1):
            f[i][j] = f[i + 1][j] # 不选第 i 个物品
            if j >= v[i]:
                # 选第 i 个物品
                f[i][j] = max(f[i][j], f[i + 1][j - v[i]] + w[i])
                
    # 2. 正向找路径
    res = []
    curr_v = V
    for i in range(1, N + 1):
        # 只要能选当前物品且选了之后能达到最优价值，就一定要选
        if curr_v >= v[i] and f[i][curr_v] == f[i + 1][curr_v - v[i]] + w[i]:
            res.append(i)
            curr_v -= v[i]
            
    # 输出结果
    print(*(res))

if __name__ == "__main__":
    solve()