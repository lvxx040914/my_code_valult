import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    begin_level = int(input_data[1])
    max_level = int(input_data[2])
    c = list(map(int, input_data[3:]))
    
    # f[i][j] 表示第 i 首歌开始前音量 j 是否可行
    # 初始化为 False
    f = [[False] * (max_level + 1) for _ in range(n + 1)]
    
    # 初始状态
    f[0][begin_level] = True
    
    # 遍历每一首歌
    for i in range(1, n + 1):
        change = c[i-1]
        has_reachable = False # 优化：检查当前这首歌是否还有存活的路径
        for j in range(max_level + 1):
            if f[i-1][j]:
                # 尝试调高
                if j + change <= max_level:
                    f[i][j + change] = True
                    has_reachable = True
                # 尝试调低
                if j - change >= 0:
                    f[i][j - change] = True
                    has_reachable = True
        
        # 如果这一步没有任何合法音量，后面肯定也没戏了
        if not has_reachable:
            print("-1")
            return

    # 从大到小找最后一首歌的最大音量
    for j in range(max_level, -1, -1):
        if f[n][j]:
            print(j)
            return
            
    print("-1")

if __name__ == "__main__":
    solve()