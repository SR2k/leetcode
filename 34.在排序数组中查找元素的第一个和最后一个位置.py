#
# @lc app=leetcode.cn id=34 lang=python3
#
# [34] 在排序数组中查找元素的第一个和最后一个位置
#
# https://leetcode.cn/problems/find-first-and-last-position-of-element-in-sorted-array/description/
#
# algorithms
# Medium (42.24%)
# Likes:    1691
# Dislikes: 0
# Total Accepted:    538.2K
# Total Submissions: 1.3M
# Testcase Example:  '[5,7,7,8,8,10]\n8'
#
# 给定一个按照升序排列的整数数组 nums，和一个目标值 target。找出给定目标值在数组中的开始位置和结束位置。
# 
# 如果数组中不存在目标值 target，返回 [-1, -1]。
# 
# 进阶：
# 
# 
# 你可以设计并实现时间复杂度为 O(log n) 的算法解决此问题吗？
# 
# 
# 
# 
# 示例 1：
# 
# 
# 输入：nums = [5,7,7,8,8,10], target = 8
# 输出：[3,4]
# 
# 示例 2：
# 
# 
# 输入：nums = [5,7,7,8,8,10], target = 6
# 输出：[-1,-1]
# 
# 示例 3：
# 
# 
# 输入：nums = [], target = 0
# 输出：[-1,-1]
# 
# 
# 
# 提示：
# 
# 
# 0 
# -10^9 
# nums 是一个非递减数组
# -10^9 
# 
# 
#

# @lc code=start
FIRST, LAST = 0, 1


class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        def b_find(flag: FIRST|LAST):
            if not nums:
                return -1

            left, right = 0, len(nums) - 1

            while left + 1 < right:
                middle = (left + right) // 2
                num_middle = nums[middle]

                if target > num_middle:
                    left = middle
                elif target < num_middle:
                    right = middle
                elif flag == FIRST:
                    right = middle
                else:
                    left = middle

            if nums[left] != target and nums[right] != target:
                return -1
            if flag == FIRST:
                if nums[left] == target:
                    return left
                else:
                    return right
            if nums[right] == target:
                return right
            else:
                return left

        return [b_find(FIRST), b_find(LAST)]
# @lc code=end
