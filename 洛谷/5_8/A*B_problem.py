a = input().strip()[::-1]
b = input().strip()[::-1]
res = [0] * (len(a) + len(b))
# 优化思路：先不处理进位，最后统一处理
for i in range(len(a)):
    for j in range(len(b)):
        res[i+j] += int(a[i]) * int(b[j])

# 统一处理进位
for i in range(len(res) - 1):
    res[i+1] += res[i] // 10
    res[i] %= 10
while len(res) > 1 and res[-1] == 0:
    res.pop()
print("".join(map(str,res[::-1])))