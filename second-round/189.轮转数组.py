#
# @lc app=leetcode.cn id=189 lang=python3
#
# [189] 轮转数组
#
# https://leetcode-cn.com/problems/rotate-array/description/
#
# algorithms
# Medium (44.58%)
# Likes:    1281
# Dislikes: 0
# Total Accepted:    413.2K
# Total Submissions: 927.4K
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
    def flip(self, nums: list[int], left: int, right: int):
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1

    def rotate(self, nums: list[int], k: int) -> None:
        n = len(nums)
        k %= n
        self.flip(nums, 0, n - k - 1)
        self.flip(nums, n - k, n - 1)
        self.flip(nums, 0, n - 1)
# @lc code=end
