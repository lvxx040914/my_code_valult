import sys

def solve():
    input_data = sys.stdin.read().split()
    
    N = int(input_data[0])
    K = int(input_data[1])
    
    # f[j] 表示余数为 j 时的最大糖果总数
    # 初始化为负无穷，表示该余数状态目前不可达
    f = [-float('inf')] * K
    f[0] = 0 # 初始总数为 0，余数为 0
    
    for i in range(N):
        w = int(input_data[i + 2])
        rem = w % K # 当前物品对 K 的余数
        
        # 拷贝当前状态，防止重复计算同一个物品（01背包特性）
        new_f = f[:]
        for j in range(K):
            # 找到能转移到当前余数 j 的前置余数 pre_j
            pre_j = (j - rem + K) % K
            if f[pre_j] != -float('inf'):
                new_f[j] = max(new_f[j], f[pre_j] + w)
        f = new_f
                
    # 结果必须是 K 的倍数，即余数为 0
    print(int(f[0]) if f[0] > 0 else 0)

if __name__ == "__main__":
    solve()