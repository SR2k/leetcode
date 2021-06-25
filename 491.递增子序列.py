#
# @lc app=leetcode.cn id=491 lang=python3
#
# [491] 递增子序列
#
# https://leetcode-cn.com/problems/increasing-subsequences/description/
#
# algorithms
# Medium (55.08%)
# Likes:    297
# Dislikes: 0
# Total Accepted:    39.4K
# Total Submissions: 71.6K
# Testcase Example:  '[4,6,7,7]'
#
# 给定一个整型数组, 你的任务是找到所有该数组的递增子序列，递增子序列的长度至少是 2 。
# 
# 
# 
# 示例：
# 
# 
# 输入：[4, 6, 7, 7]
# 输出：[[4, 6], [4, 7], [4, 6, 7], [4, 6, 7, 7], [6, 7], [6, 7, 7], [7,7],
# [4,7,7]]
# 
# 
# 
# 提示：
# 
# 
# 给定数组的长度不会超过15。
# 数组中的整数范围是 [-100,100]。
# 给定数组中可能包含重复数字，相等的数字应该被视为递增的一种情况。
# 
# 
#

# @lc code=start
class Solution:
    def findSubsequences(self, nums: list[int]) -> list[list[int]]:
        ret: list[list[int]] = []
        length = len(nums)

        def helper(i: int, curr: list[int]):
            if i >= length:
                return

            repeat_end = i
            while repeat_end < length - 1 and nums[repeat_end] == nums[repeat_end + 1]:
                repeat_end += 1
            repeat_count = repeat_end - i + 1

            if not curr or nums[i] >= curr[-1]:
                for _ in range(repeat_count):
                    curr.append(nums[i])
                    if len(curr) > 1: ret.append(curr + [])
                    helper(i + repeat_count, curr)
                for _ in range(repeat_count):
                    curr.pop()

            helper(i + repeat_count, curr)

        helper(0, [])
        return ret


# @lc code=end

print(Solution().findSubsequences([4, 6, 7, 7]))
