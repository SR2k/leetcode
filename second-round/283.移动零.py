#
# @lc app=leetcode.cn id=283 lang=python3
#
# [283] 移动零
#
# https://leetcode-cn.com/problems/move-zeroes/description/
#
# algorithms
# Easy (64.03%)
# Likes:    1395
# Dislikes: 0
# Total Accepted:    595.7K
# Total Submissions: 930.4K
# Testcase Example:  '[0,1,0,3,12]'
#
# 给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。
# 
# 示例:
# 
# 输入: [0,1,0,3,12]
# 输出: [1,3,12,0,0]
# 
# 说明:
# 
# 
# 必须在原数组上操作，不能拷贝额外的数组。
# 尽量减少操作次数。
# 
# 
#

# @lc code=start
class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        i, p = 0, 0

        while i < len(nums): # F IXME
            while i + 1 < len(nums) and nums[i] == 0:
                i += 1
            nums[p] = nums[i]
            i += 1
            p += 1

        for i in range(p, len(nums)):
            nums[i] = 0
# @lc code=end

q = Solution()
s = [0,1,0,3,12]
q.moveZeroes(s)
print(s)
s = [0,0,0,0,0]
q.moveZeroes(s)
print(s)
s = []
q.moveZeroes(s)
print(s)
s = [1,2,0,0]
q.moveZeroes(s)
print(s)
