import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    m = int(input_data[1])
    a = list(map(int, input_data[2:]))
    MOD = 10007
    
    # 预处理组合数 C(n, k)
    # 因为 a_i <= 100, 所以我们只需要预处理到 k=100 即可
    # C[i][j] 表示从 i 个里选 j 个
    C = [[0] * 101 for _ in range(n + 1)]
    
    for i in range(n + 1):
        C[i][0] = 1
        for j in range(1, min(i, 100) + 1):
            C[i][j] = (C[i-1][j-1] + C[i-1][j]) % MOD
            
    ans = 1
    current_n = n
    for count in a:
        if count == 0:
            continue
        # 乘以当前步骤的组合数
        ans = (ans * C[current_n][count]) % MOD
        # 减去已经分出去的牌
        current_n -= count
        
    print(ans)

if __name__ == "__main__":
    solve()