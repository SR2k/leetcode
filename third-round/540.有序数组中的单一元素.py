#
# @lc app=leetcode.cn id=540 lang=python3
#
# [540] 有序数组中的单一元素
#
# https://leetcode-cn.com/problems/single-element-in-a-sorted-array/description/
#
# algorithms
# Medium (61.02%)
# Likes:    480
# Dislikes: 0
# Total Accepted:    88.8K
# Total Submissions: 145.7K
# Testcase Example:  '[1,1,2,3,3,4,4,8,8]'
#
# 给你一个仅由整数组成的有序数组，其中每个元素都会出现两次，唯有一个数只会出现一次。
# 
# 请你找出并返回只出现一次的那个数。
# 
# 你设计的解决方案必须满足 O(log n) 时间复杂度和 O(1) 空间复杂度。
# 
# 
# 
# 示例 1:
# 
# 
# 输入: nums = [1,1,2,3,3,4,4,8,8]
# 输出: 2
# 
# 
# 示例 2:
# 
# 
# 输入: nums =  [3,3,7,7,10,11,11]
# 输出: 10
# 
# 
# 
# 
# 
# 
# 提示:
# 
# 
# 1 <= nums.length <= 10^5
# 0 <= nums[i] <= 10^5
# 
# 
#

# @lc code=start
class Solution:
    def singleNonDuplicate(self, nums: list[int]) -> int:
        left, right = 0, len(nums) - 1

        while left + 1 < right:
            middle = (left + right) >> 1

            if self.check(nums, middle):
                left = middle
            else:
                right = middle

        if not self.check(nums, left):
            return nums[left]
        return nums[right]

    def check(self, nums: list[int], i: int):
        if i % 2:
            return i - 1 >= 0 and nums[i] == nums[i - 1]
        else:
            return i + 1 < len(nums) and nums[i] == nums[i + 1]
# @lc code=end

print(Solution().singleNonDuplicate([1,1,2,3,3,4,4,8,8]))
print(Solution().singleNonDuplicate([3,3,7,7,10,11,11]))
print(Solution().singleNonDuplicate([1,3,3]))
print(Solution().singleNonDuplicate([3,3,1]))
print(Solution().singleNonDuplicate([1]))
