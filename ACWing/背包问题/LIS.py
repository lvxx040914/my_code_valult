# def lis(nums):
#     if not nums:
#         return 0
#     dp = [1]*len(nums)
#     for i in range(len(nums)):
#         for j in range(i):
#             if nums[i]>nums[j]:
#                 dp[i]=max(dp[i],dp[j]+1)
#     return max(dp)

import bisect

def lis(nums):
    res = []
    for num in nums:
        i = bisect.bisect_left(res, num)
        if i == len(res):
            res.append(num)
        else:
            res[i] = num
    return len(res)