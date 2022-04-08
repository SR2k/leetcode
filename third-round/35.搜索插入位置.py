#
# @lc app=leetcode.cn id=35 lang=python3
#
# [35] 搜索插入位置
#
# https://leetcode-cn.com/problems/search-insert-position/description/
#
# algorithms
# Easy (45.63%)
# Likes:    1369
# Dislikes: 0
# Total Accepted:    678.6K
# Total Submissions: 1.5M
# Testcase Example:  '[1,3,5,6]\n5'
#
# 给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。
# 
# 请必须使用时间复杂度为 O(log n) 的算法。
# 
# 
# 
# 示例 1:
# 
# 
# 输入: nums = [1,3,5,6], target = 5
# 输出: 2
# 
# 
# 示例 2:
# 
# 
# 输入: nums = [1,3,5,6], target = 2
# 输出: 1
# 
# 
# 示例 3:
# 
# 
# 输入: nums = [1,3,5,6], target = 7
# 输出: 4
# 
# 
# 示例 4:
# 
# 
# 输入: nums = [1,3,5,6], target = 0
# 输出: 0
# 
# 
# 示例 5:
# 
# 
# 输入: nums = [1], target = 0
# 输出: 0
# 
# 
# 
# 
# 提示:
# 
# 
# 1 
# -10^4 
# nums 为无重复元素的升序排列数组
# -10^4 
# 
# 
#

# @lc code=start
class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left + 1 < right:
            middle = (left + right) >> 1
            num_middle = nums[middle]

            if num_middle >= target:
                right = middle
            else:
                left = middle

        if nums[left] >= target:
            return left
        if nums[right] >= target:
            return right
        return len(nums)
# @lc code=end

print(Solution().searchInsert([1,3,5,6], target = 5))
print(Solution().searchInsert([1,3,5,6], target = 2))
print(Solution().searchInsert([1,3,5,6], target = 7))
print(Solution().searchInsert([1,3,5,6], target = 0))
print(Solution().searchInsert([1], target = 0))
