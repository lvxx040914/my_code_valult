import sys

input_data = sys.stdin.read().split()
idx = 0
check = [100, 50, 10, 5, 2, 1]

while idx < len(input_data):
    n = int(input_data[idx])
    
    # 提取当前组的 n 个工资数值
    a = list(map(int, input_data[idx + 1 : idx + n + 1]))
    idx += n + 1
    
    cnt = 0
    for c in a:
        for i in range(6):
            if c >= check[i]:
                # 优化：直接计算能放多少张，剩下的取余
                cnt += c // check[i]
                c %= check[i]
    print(cnt)