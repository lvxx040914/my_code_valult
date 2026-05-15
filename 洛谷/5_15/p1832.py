import sys

def solve():
    n = int(sys.stdin.read().strip())
    
    # 1. 筛选素数 (埃氏筛)
    is_prime = [True] * (n + 1)
    primes = []
    for i in range(2, n + 1):
        if is_prime[i]:
            primes.append(i)
            for j in range(i * i, n + 1, i):
                is_prime[j] = False
                
    # 2. 完全背包求方案数
    # dp[j] 表示和为 j 的方案数
    dp = [0] * (n + 1)
    dp[0] = 1 # 基础状态
    
    for p in primes:
        # 正序遍历表示每个素数可以取无限次
        for j in range(p, n + 1):
            dp[j] += dp[j - p]
            
    print(dp[n])

if __name__ == "__main__":
    solve()