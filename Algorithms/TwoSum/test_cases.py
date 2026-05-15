from solution import Solution

def run_test():
    sol = Solution()
    
    # 测试用例格式: (nums, target, expected_answer)
    test_cases = [
        ([2, 7, 11, 15], 9, [0, 1]),
        ([3, 2, 4], 6, [1, 2]),
        ([3, 3], 6, [0, 1]),
    ]
    
    for i, (nums, target, expected) in enumerate(test_cases):
        result = sol.twoSum(nums, target)
        # 排序是因为返回的下标顺序可能不同，不影响逻辑
        if sorted(result) == sorted(expected):
            print(f"Case {i+1}: Passed! ✅")
        else:
            print(f"Case {i+1}: Failed! ❌ (Expected {expected}, got {result})")

if __name__ == "__main__":
    run_test()