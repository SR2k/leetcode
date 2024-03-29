#
# @lc app=leetcode.cn id=1760 lang=python3
#
# [1760] 袋子里最少数目的球
#
# https://leetcode-cn.com/problems/minimum-limit-of-balls-in-a-bag/description/
#
# algorithms
# Medium (53.71%)
# Likes:    51
# Dislikes: 0
# Total Accepted:    4.1K
# Total Submissions: 7.5K
# Testcase Example:  '[9]\n2'
#
# 给你一个整数数组 nums ，其中 nums[i] 表示第 i 个袋子里球的数目。同时给你一个整数 maxOperations 。
# 
# 你可以进行如下操作至多 maxOperations 次：
# 
# 
# 选择任意一个袋子，并将袋子里的球分到 2 个新的袋子中，每个袋子里都有 正整数 个球。
# 
# 
# 比方说，一个袋子里有 5 个球，你可以把它们分到两个新袋子里，分别有 1 个和 4 个球，或者分别有 2 个和 3 个球。
# 
# 
# 
# 
# 你的开销是单个袋子里球数目的 最大值 ，你想要 最小化 开销。
# 
# 请你返回进行上述操作后的最小开销。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：nums = [9], maxOperations = 2
# 输出：3
# 解释：
# - 将装有 9 个球的袋子分成装有 6 个和 3 个球的袋子。[9] -> [6,3] 。
# - 将装有 6 个球的袋子分成装有 3 个和 3 个球的袋子。[6,3] -> [3,3,3] 。
# 装有最多球的袋子里装有 3 个球，所以开销为 3 并返回 3 。
# 
# 
# 示例 2：
# 
# 
# 输入：nums = [2,4,8,2], maxOperations = 4
# 输出：2
# 解释：
# - 将装有 8 个球的袋子分成装有 4 个和 4 个球的袋子。[2,4,8,2] -> [2,4,4,4,2] 。
# - 将装有 4 个球的袋子分成装有 2 个和 2 个球的袋子。[2,4,4,4,2] -> [2,2,2,4,4,2] 。
# - 将装有 4 个球的袋子分成装有 2 个和 2 个球的袋子。[2,2,2,4,4,2] -> [2,2,2,2,2,4,2] 。
# - 将装有 4 个球的袋子分成装有 2 个和 2 个球的袋子。[2,2,2,2,2,4,2] -> [2,2,2,2,2,2,2,2] 。
# 装有最多球的袋子里装有 2 个球，所以开销为 2 并返回 2 。
# 
# 
# 示例 3：
# 
# 
# 输入：nums = [7,17], maxOperations = 2
# 输出：7
# 
# 
# 
# 
# 提示：
# 
# 
# 1 
# 1 
# 
# 
#

# @lc code=start
from math import ceil


class Solution:
    @staticmethod
    def check(nums: list[int], target: int, max_operations: int) -> bool:
        for n in nums:
            if n <= target:
                continue
            max_operations -= ceil(n / target) - 1

            if max_operations < 0:
                return False
        return True

    def minimumSize(self, nums: list[int], maxOperations: int) -> int:
        left, right = 1, max(nums)

        while left + 1 < right:
            middle = (left + right) // 2

            if Solution.check(nums, middle, maxOperations):
                right = middle
            else:
                left = middle

        if Solution.check(nums, left, maxOperations):
            return left
        return right
# @lc code=end

s = Solution()
print(s.minimumSize(nums = [9], maxOperations = 2))
print(s.minimumSize(nums = [2,4,8,2], maxOperations = 4))
print(s.minimumSize(nums = [7,17], maxOperations = 2))
