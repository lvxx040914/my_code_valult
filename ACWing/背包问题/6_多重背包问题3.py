import sys
from collections import deque

def solve():
    # 使用 fast I/O
    input_data = sys.stdin.read().split()
    
    N = int(input_data[0])
    V = int(input_data[1])
    idx = 2
    
    dp = [0] * (V + 1)

    for _ in range(N):
        v = int(input_data[idx]); idx += 1
        w = int(input_data[idx]); idx += 1
        s = int(input_data[idx]); idx += 1
        
        # 拷贝当前状态，避免更新过程中的污染
        g = dp[:]
        
        # 按余数 r 分组
        for r in range(v):
            queue = deque()
            # 遍历每个分组中的容量 j = q * v + r
            for q in range((V - r) // v + 1):
                # 当前待入队的值：g[k*v + r] - k*w
                val = g[q * v + r] - q * w
                
                # 维护单调递减队列
                while queue and queue[-1][1] <= val:
                    queue.pop()
                queue.append((q, val))
                
                # 移除滑出窗口的元素 (窗口大小为 s)
                if queue[0][0] < q - s:
                    queue.popleft()
                
                # 更新 dp 值：max_val + q * w
                dp[q * v + r] = queue[0][1] + q * w

    print(dp[V])

if __name__ == "__main__":
    solve()