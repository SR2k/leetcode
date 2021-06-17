#
# @lc app=leetcode.cn id=31 lang=python3
#
# [31] 下一个排列
#
# https://leetcode-cn.com/problems/next-permutation/description/
#
# algorithms
# Medium (36.85%)
# Likes:    1154
# Dislikes: 0
# Total Accepted:    171.3K
# Total Submissions: 463.3K
# Testcase Example:  '[1,2,3]'
#
# 实现获取 下一个排列 的函数，算法需要将给定数字序列重新排列成字典序中下一个更大的排列。
# 
# 如果不存在下一个更大的排列，则将数字重新排列成最小的排列（即升序排列）。
# 
# 必须 原地 修改，只允许使用额外常数空间。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：nums = [1,2,3]
# 输出：[1,3,2]
# 
# 
# 示例 2：
# 
# 
# 输入：nums = [3,2,1]
# 输出：[1,2,3]
# 
# 
# 示例 3：
# 
# 
# 输入：nums = [1,1,5]
# 输出：[1,5,1]
# 
# 
# 示例 4：
# 
# 
# 输入：nums = [1]
# 输出：[1]
# 
# 
# 
# 
# 提示：
# 
# 
# 1 
# 0 
# 
# 
#

# @lc code=start
class Solution:
    def findFirstGreater(self, nums: list[int], target: int, left: int, right: int):
        while left + 1 < right:
            middle = math.floor((left + right) / 2)
            if nums[middle] <= target:
                right = middle
            else:
                left = middle
        if nums[right] > target: return right
        return left

    def nextPermutation(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] < nums[i + 1]: break
        firstGreater = self.findFirstGreater(nums, nums[i], i + 1, len(nums) - 1)
        nums[i], nums[firstGreater] = nums[firstGreater], nums[i]
        nums[i + 1:] = sorted(nums[i + 1:])
# @lc code=end

# nums = [1,3,2]
# Solution().nextPermutation(nums)
# print(nums)
