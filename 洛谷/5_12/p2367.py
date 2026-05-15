import sys

def solve():
    # 使用 fast I/O 处理 500w 数据
    input = sys.stdin.read().split()
    if not input:
        return
    
    n = int(input[0])
    p = int(input[1])
    
    # 原始成绩
    a = list(map(int, input[2 : 2 + n]))
    
    # 1. 构造差分数组 (多开一位防止 y+1 越界)
    # diff[i] 存储 a[i] - a[i-1]
    diff = [0] * (n + 2)
    
    # 初始化差分数组
    diff[0] = a[0]
    for i in range(1, n):
        diff[i] = a[i] - a[i-1]
        
    # 2. 区间修改
    current_pos = 2 + n
    for _ in range(p):
        x = int(input[current_pos])
        y = int(input[current_pos + 1])
        z = int(input[current_pos + 2])
        current_pos += 3
        
        # 对应到 0-indexed：区间 [x-1, y-1]
        diff[x-1] += z
        diff[y] -= z  # 修正 y 位置之后（即 y-1 + 1）的值

    # 3. 还原数组并求最小值
    min_score = float('inf')
    current_val = 0
    for i in range(n):
        current_val += diff[i] # 差分的前缀和就是修改后的原值
        if current_val < min_score:
            min_score = current_val
            
    print(min_score)

if __name__ == "__main__":
    solve()