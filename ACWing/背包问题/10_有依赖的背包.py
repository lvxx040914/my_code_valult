import sys

# 增加递归深度，防止树太深
sys.setrecursionlimit(2000)

def solve():
    input_data = sys.stdin.read().split()
    
    ptr = 0
    n = int(input_data[ptr]); ptr += 1
    v_limit = int(input_data[ptr]); ptr += 1
    
    # 存储物品信息
    v = [0] * (n + 1)
    w = [0] * (n + 1)
    adj = [[] for _ in range(n + 1)]
    root = -1
    
    for i in range(1, n + 1):
        vi = int(input_data[ptr]); ptr += 1
        wi = int(input_data[ptr]); ptr += 1
        pi = int(input_data[ptr]); ptr += 1
        v[i], w[i] = vi, wi
        if pi == -1:
            root = i
        else:
            adj[pi].append(i)
            
    # f[u][j] 表示以u为根的子树容量为j时的最大价值
    f = [[0] * (v_limit + 1) for _ in range(n + 1)]
    
    def dfs(u):
        # 只要选子树，就必须选根节点u，先初始化分配给u的价值
        for j in range(v[u], v_limit + 1):
            f[u][j] = w[u]
        
        # 遍历子节点（物品组）
        for s in adj[u]:
            dfs(s)
            # 分组背包：逆序遍历容量，确保每个子树（组）只选一种体积分配方案
            for j in range(v_limit, v[u] - 1, -1):
                # 预留出父节点 u 的体积 v[u]，剩下的 j - v[u] 分配给子树
                for k in range(j - v[u] + 1):
                    f[u][j] = max(f[u][j], f[u][j - k] + f[s][k])
                    
    dfs(root)
    print(f[root][v_limit])

if __name__ == "__main__":
    solve()