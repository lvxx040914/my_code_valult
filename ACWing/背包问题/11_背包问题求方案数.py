import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    N = int(input_data[0])
    V = int(input_data[1])
    MOD = 10**9 + 7
    
    # f[j] 存储容量为 j 时的最大价值
    f = [0] * (V + 1)
    # g[j] 存储容量为 j 时达到最大价值的方案数
    g = [1] * (V + 1)
    
    idx = 2
    for _ in range(N):
        v = int(input_data[idx]); idx += 1
        w = int(input_data[idx]); idx += 1
        
        # 01 背包逆序遍历容量
        for j in range(V, v - 1, -1):
            new_val = f[j - v] + w
            
            if new_val > f[j]:
                # 情况 1：选择新物品价值更高
                f[j] = new_val
                g[j] = g[j - v]
            elif new_val == f[j]:
                # 情况 2：价值相等，累加方案数
                g[j] = (g[j] + g[j - v]) % MOD
            # 情况 3：new_val < f[j]，保持现状即可
                
    # 注意：最终答案不一定是 g[V]，因为最大价值可能在 j < V 时就已经达到
    # 但由于本题中物品价值 wi > 0，通常 f[V] 就是最大价值。
    # 为了保险，可以遍历一遍找到真正的最大价值对应的方案数
    
    print(g[V])

if __name__ == "__main__":
    solve()


# import sys

# def solve():
#     input_data = sys.stdin.read().split()
#     N,V = int(input_data[0]),int(input_data[1])
#     MOD = 10**9 + 7
#     f = [0] * (V + 1)
#     g = [1] * (V + 1)
#     idx = 2
#     for _ in range(N):
#         v,w = int(input_data[idx]),int(input_data[idx+1])
#         idx += 2
        
#         for j in range(V,v-1,-1):
#             new_val = f[j-v]+w
#             if new_val > f[j]:
#                 f[j] = new_val
#                 g[j] = g[j-v]
#             elif new_val == f[j]:
#                 g[j] = (g[j]+g[j-v])%MOD
#     print(g[V])

# if __name__ == "__main__":
#     solve()