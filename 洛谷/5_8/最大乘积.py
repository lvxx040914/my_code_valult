import sys

n = int(sys.stdin.read().strip())
if n == 3 or n == 4:
    print(str(n))
    print(n)
else:
    nums = []
    cur_sum = 0
    for i in range(2,n+1):
        if cur_sum + i <= n:
            nums.append(i)
            cur_sum += i
        else:
            break
    re = n - cur_sum
    idx = len(nums) - 1
    while re > 0:
        nums[idx] += 1
        re -= 1
        idx -= 1
        if idx < 0:
            idx = len(nums) - 1
    print(*(nums))

    sys.set_int_max_str_digits(20000)
    res = 1
    for x in nums:
        res *= x
    print(res)