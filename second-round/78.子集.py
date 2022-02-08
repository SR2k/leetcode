#
# @lc app=leetcode.cn id=78 lang=python3
#
# [78] 子集
#
# https://leetcode-cn.com/problems/subsets/description/
#
# algorithms
# Medium (80.27%)
# Likes:    1454
# Dislikes: 0
# Total Accepted:    359.7K
# Total Submissions: 448.2K
# Testcase Example:  '[1,2,3]'
#
# 给你一个整数数组 nums ，数组中的元素 互不相同 。返回该数组所有可能的子集（幂集）。
# 
# 解集 不能 包含重复的子集。你可以按 任意顺序 返回解集。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：nums = [1,2,3]
# 输出：[[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
# 
# 
# 示例 2：
# 
# 
# 输入：nums = [0]
# 输出：[[],[0]]
# 
# 
# 
# 
# 提示：
# 
# 
# 1 
# -10 
# nums 中的所有元素 互不相同
# 
# 
#

# @lc code=start
class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        result = []
        len_nums = len(nums)

        def helper(prev: list[int], i: int, n: int):
            if i >= len_nums:
                if len(prev) == n:
                    result.append([n for n in prev])
                return

            if len(prev) < n:
                prev.append(nums[i])
                helper(prev, i + 1, n)
                prev.pop()

            helper(prev, i + 1, n)

        for cnt in range(len(nums) + 1):
            helper([], 0, cnt)

        return result
# @lc code=end

s = Solution()
print(s.subsets([]))
print(s.subsets([0,1]))
print(s.subsets([0,1,2]))
print(s.subsets([0,1,2,3]))
