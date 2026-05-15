import sys

def solve():
    # 使用快读
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    x = int(input_data[1])
    
    # dp[j] 表示用 j 个药水能获得的最大经验
    dp = [0] * (x + 1)
    
    ptr = 2
    for _ in range(n):
        lose = int(input_data[ptr])
        win = int(input_data[ptr+1])
        use = int(input_data[ptr+2])
        ptr += 3
        
        # 01 背包逆序遍历容量
        for j in range(x, -1, -1):
            if j >= use:
                # 够药：比一下 (之前的经验+这次输) 和 (扣掉药水赢了后的经验)
                dp[j] = max(dp[j] + lose, dp[j - use] + win)
            else:
                # 不够药：强制拿失败经验
                dp[j] += lose
                
    # 输出 5 倍结果
    print(dp[x] * 5)

if __name__ == "__main__":
    solve()