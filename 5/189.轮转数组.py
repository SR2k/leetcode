#
# @lc app=leetcode.cn id=189 lang=python3
#
# [189] 轮转数组
#
# https://leetcode.cn/problems/rotate-array/description/
#
# algorithms
# Medium (44.32%)
# Likes:    1485
# Dislikes: 0
# Total Accepted:    501.6K
# Total Submissions: 1.1M
# Testcase Example:  '[1,2,3,4,5,6,7]\n3'
#
# 给你一个数组，将数组中的元素向右轮转 k 个位置，其中 k 是非负数。
# 
# 
# 
# 示例 1:
# 
# 
# 输入: nums = [1,2,3,4,5,6,7], k = 3
# 输出: [5,6,7,1,2,3,4]
# 解释:
# 向右轮转 1 步: [7,1,2,3,4,5,6]
# 向右轮转 2 步: [6,7,1,2,3,4,5]
# 向右轮转 3 步: [5,6,7,1,2,3,4]
# 
# 
# 示例 2:
# 
# 
# 输入：nums = [-1,-100,3,99], k = 2
# 输出：[3,99,-1,-100]
# 解释: 
# 向右轮转 1 步: [99,-1,-100,3]
# 向右轮转 2 步: [3,99,-1,-100]
# 
# 
# 
# 提示：
# 
# 
# 1 <= nums.length <= 10^5
# -2^31 <= nums[i] <= 2^31 - 1
# 0 <= k <= 10^5
# 
# 
# 
# 
# 进阶：
# 
# 
# 尽可能想出更多的解决方案，至少有 三种 不同的方法可以解决这个问题。
# 你可以使用空间复杂度为 O(1) 的 原地 算法解决这个问题吗？
# 
# 
# 
# 
# 
# 
# 
# 
#

# @lc code=start
class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        k %= len(nums)
        if k == 0:
            return

        Solution.reverse(nums, len(nums) - k, len(nums) - 1)
        Solution.reverse(nums, 0, len(nums) - k - 1)
        Solution.reverse(nums, 0, len(nums) - 1)


    @staticmethod
    def reverse(nums: list, i: int, j: int):
        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1
# @lc code=end
