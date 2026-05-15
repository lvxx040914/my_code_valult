import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    ptr = 0
    n = int(input_data[ptr]); ptr += 1
    m = int(input_data[ptr]); ptr += 1
    k_limit = int(input_data[ptr]); ptr += 1
    r_total = int(input_data[ptr]); ptr += 1
    
    # 刷题所需时间列表
    solve_times = []
    for _ in range(n):
        solve_times.append(int(input_data[ptr]))
        ptr += 1
        
    # 作业所需时间
    job_costs = []
    for _ in range(m):
        job_costs.append(int(input_data[ptr]))
        ptr += 1
        
    # 作业对应分值
    job_scores = []
    for _ in range(m):
        job_scores.append(int(input_data[ptr]))
        ptr += 1
        
    # --- 阶段一：01背包算作业 ---
    # dp[j] 表示花费时间 j 能拿到的最高分
    dp = [0] * (r_total + 1)
    for i in range(m):
        cost = job_costs[i]
        score = job_scores[i]
        for j in range(r_total, cost - 1, -1):
            if dp[j - cost] + score > dp[j]:
                dp[j] = dp[j - cost] + score
                
    # 寻找及格（>= k_limit）所需的最少时间
    min_t = 0
    for t in range(r_total + 1):
        if dp[t] >= k_limit:
            min_t = t
            break
            
    rest_time = r_total - min_t
    
    # --- 阶段二：贪心刷题 ---
    solve_times.sort() # 耗时短的优先
    ans = 0
    for t in solve_times:
        if rest_time >= t:
            rest_time -= t
            ans += 1
        else:
            break
            
    print(ans)

if __name__ == "__main__":
    solve()