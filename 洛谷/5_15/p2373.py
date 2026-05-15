import sys

def solve():
    # 读取输入的 6 个数字
    line = sys.stdin.read().split()
    a = list(map(int, line))

    # 砝码的面值
    weights = [1, 2, 3, 5, 10, 20]
    
    # dp[j] 表示重量 j 是否可以称出
    # 最大重量不超过 1000
    max_w = 1000
    dp = [False] * (max_w + 1)
    dp[0] = True # 初始状态，重量 0 是可达的（虽然最后不计入结果）
    
    # 遍历 6 种砝码
    for i in range(6):
        w = weights[i] # 当前砝码重量
        num = a[i]     # 当前砝码个数
        
        # 对每一个砝码，我们都要更新一次 DP 表 (01背包思想)
        # 为了防止同一种砝码的多个个数在一次更新中重叠，
        # 我们需要循环 num 次，且每次逆序遍历容量
        for _ in range(num):
            for j in range(max_w, w - 1, -1):
                if dp[j - w]:
                    dp[j] = True
                    
    # 统计 True 的个数，排除重量 0
    ans = sum(dp[1:])
    print(f"Total={ans}")

if __name__ == "__main__":
    solve()