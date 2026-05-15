import sys

def zero_one_pack(dp, v, w):
    for i in range(len(dp)-1, v-1, -1):
        dp[i] = max(dp[i], dp[i-v] + w)

def complete_pack(dp, v, w):
    for i in range(v, len(dp)):
        dp[i] = max(dp[i], dp[i-v] + w)

def multiple_pack(dp, v, w, s):
    if v * s >= len(dp):
        complete_pack(dp, v, w)
    else:
        k = 1
        while k <= s:
            zero_one_pack(dp, k*v, k*w)
            s -= k
            k *= 2
        if s > 0:
            zero_one_pack(dp, s*v, s*w)

def solve():
    input_data = sys.stdin.read().split()
    
    N,V = int(input_data[0]),int(input_data[1])
    dp = [0] * (V + 1)
    cur_idx = 2
    new_items = []
    for _ in range(N):
        v = int(input_data[cur_idx])
        w = int(input_data[cur_idx + 1])
        s = int(input_data[cur_idx + 2])
        cur_idx += 3
        
        if s == -1:
            zero_one_pack(dp, v, w)
        elif s == 0:
            complete_pack(dp, v, w)
        else:
            multiple_pack(dp, v, w, s)
    print(dp[-1])

if __name__ == "__main__":
    solve()