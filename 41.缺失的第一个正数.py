#
# @lc app=leetcode.cn id=41 lang=python3
#
# [41] 缺失的第一个正数
#
# https://leetcode-cn.com/problems/first-missing-positive/description/
#
# algorithms
# Hard (41.36%)
# Likes:    1113
# Dislikes: 0
# Total Accepted:    139.3K
# Total Submissions: 336.8K
# Testcase Example:  '[1,2,0]'
#
# 给你一个未排序的整数数组 nums ，请你找出其中没有出现的最小的正整数。
# 请你实现时间复杂度为 O(n) 并且只使用常数级别额外空间的解决方案。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：nums = [1,2,0]
# 输出：3
# 
# 
# 示例 2：
# 
# 
# 输入：nums = [3,4,-1,1]
# 输出：2
# 
# 
# 示例 3：
# 
# 
# 输入：nums = [7,8,9,11,12]
# 输出：1
# 
# 
# 
# 
# 提示：
# 
# 
# 1 
# -2^31 
# 
# 
#

# @lc code=start
class Solution:
    def firstMissingPositive(self, nums: list[int]) -> int:
        n = len(nums)
        has_1 = False
        for i in range(n):
            if nums[i] == 1:
                has_1 = True
            if nums[i] <= 0 or nums[i] > n:
                nums[i] = 1
        if not has_1:
            return 1

        for num in nums:
            idx = abs(num) - 1
            nums[idx] = -abs(nums[idx])

        for i in range(n):
            if nums[i] > 0:
                return i + 1
        return n + 1
# @lc code=end

