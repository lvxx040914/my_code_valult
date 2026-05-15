from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        :param nums: 输入整数数组
        :param target: 目标值
        :return: 目标值对应的两个整数的下标
        """
        # --- 进阶方法：哈希表 (Hash Map) ---
        # 时间复杂度: O(n)
        # 空间复杂度: O(n)
        hashtable = dict()
        for i, num in enumerate(nums):
            complement = target - num
            if complement in hashtable:
                return [hashtable[complement], i]
            hashtable[num] = i
        
        return []

# 这里留出空白，方便你自己尝试暴力解法 (双重循环)