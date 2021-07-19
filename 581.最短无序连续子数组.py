#
# @lc app=leetcode.cn id=581 lang=python3
#
# [581] 最短无序连续子数组
#
# https://leetcode-cn.com/problems/shortest-unsorted-continuous-subarray/description/
#
# algorithms
# Medium (37.22%)
# Likes:    569
# Dislikes: 0
# Total Accepted:    62.4K
# Total Submissions: 167.6K
# Testcase Example:  '[2,6,4,8,10,9,15]'
#
# 给你一个整数数组 nums ，你需要找出一个 连续子数组 ，如果对这个子数组进行升序排序，那么整个数组都会变为升序排序。
# 
# 请你找出符合题意的 最短 子数组，并输出它的长度。
# 
# 
# 
# 
# 
# 示例 1：
# 
# 
# 输入：nums = [2,6,4,8,10,9,15]
# 输出：5
# 解释：你只需要对 [6, 4, 8, 10, 9] 进行升序排序，那么整个表都会变为升序排序。
# 
# 
# 示例 2：
# 
# 
# 输入：nums = [1,2,3,4]
# 输出：0
# 
# 
# 示例 3：
# 
# 
# 输入：nums = [1]
# 输出：0
# 
# 
# 
# 
# 提示：
# 
# 
# 1 
# -10^5 
# 
# 
# 
# 
# 进阶：你可以设计一个时间复杂度为 O(n) 的解决方案吗？
# 
# 
# 
#

# @lc code=start
# class Solution:
#     def findUnsortedSubarray(self, nums: list[int]) -> int:
#         sorted_nums = sorted(nums)
#         left, right = 0, len(nums) - 1
#         len_nums = len(nums)

#         while left < len_nums and sorted_nums[left] == nums[left ]:
#             left += 1
#         while right >= 0 and sorted_nums[right] == nums[right]:
#             right -= 1

#         ret = right - left + 1
#         return max(ret, 0)

class Solution:
    def findUnsortedSubarray(self, nums: list[int]) -> int:
        stack: list[int] = []
        left = len(nums)
        for i, n in enumerate(nums):
            while stack and nums[stack[-1]] > n:
                left = min(stack.pop(), left)
            stack.append(i)

        stack = []
        right = -1
        for i in range(len(nums) - 1, -1, -1):
            while stack and nums[stack[-1]] < nums[i]:
                right = max(stack.pop(), right)
            stack.append(i)

        return max(0, right - left + 1)
# @lc code=end
