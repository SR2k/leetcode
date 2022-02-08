#
# @lc app=leetcode.cn id=46 lang=python3
#
# [46] 全排列
#
# https://leetcode-cn.com/problems/permutations/description/
#
# algorithms
# Medium (78.45%)
# Likes:    1731
# Dislikes: 0
# Total Accepted:    490.6K
# Total Submissions: 625.3K
# Testcase Example:  '[1,2,3]'
#
# 给定一个不含重复数字的数组 nums ，返回其 所有可能的全排列 。你可以 按任意顺序 返回答案。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：nums = [1,2,3]
# 输出：[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
# 
# 
# 示例 2：
# 
# 
# 输入：nums = [0,1]
# 输出：[[0,1],[1,0]]
# 
# 
# 示例 3：
# 
# 
# 输入：nums = [1]
# 输出：[[1]]
# 
# 
# 
# 
# 提示：
# 
# 
# 1 
# -10 
# nums 中的所有整数 互不相同
# 
# 
#

# @lc code=start
class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        result = []

        def helper(nums: list[int], left: int, right: int):
            if left == right:
                result.append([n for n in nums])

            for i in range(left, right + 1):
                nums[left], nums[i] = nums[i], nums[left]
                helper(nums, left + 1, right)
                nums[left], nums[i] = nums[i], nums[left]

        helper(nums, 0, len(nums) - 1)
        return result
# @lc code=end

s = Solution()
print(s.permute([1,2,3]))
print(s.permute([0,1]))
print(s.permute([1]))
