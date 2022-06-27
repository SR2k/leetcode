#
# @lc app=leetcode.cn id=41 lang=python3
#
# [41] 缺失的第一个正数
#
# https://leetcode.cn/problems/first-missing-positive/description/
#
# algorithms
# Hard (42.56%)
# Likes:    1471
# Dislikes: 0
# Total Accepted:    222K
# Total Submissions: 521.3K
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
        for i, n in enumerate(nums):
            if n < 0:
                nums[i] = 0

        for n in nums:
            if n <= 0:
                n = -n - 1
            if 1 <= n <= len(nums) and nums[n - 1] >= 0:
                nums[n - 1] = -nums[n - 1] - 1

        for i, n in enumerate(nums):
            if n >= 0:
                return i + 1

        return len(nums) + 1
# @lc code=end
