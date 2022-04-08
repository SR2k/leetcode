#
# @lc app=leetcode.cn id=77 lang=python3
#
# [77] 组合
#
# https://leetcode-cn.com/problems/combinations/description/
#
# algorithms
# Medium (77.01%)
# Likes:    931
# Dislikes: 0
# Total Accepted:    320.7K
# Total Submissions: 416.4K
# Testcase Example:  '4\n2'
#
# 给定两个整数 n 和 k，返回范围 [1, n] 中所有可能的 k 个数的组合。
# 
# 你可以按 任何顺序 返回答案。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：n = 4, k = 2
# 输出：
# [
# ⁠ [2,4],
# ⁠ [3,4],
# ⁠ [2,3],
# ⁠ [1,2],
# ⁠ [1,3],
# ⁠ [1,4],
# ]
# 
# 示例 2：
# 
# 
# 输入：n = 1, k = 1
# 输出：[[1]]
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
class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:
        result = []

        def helper(i: int, prev: list[int]):
            if len(prev) == k:
                result.append(prev + [])
                return
            if i > n:
                return

            prev.append(i)
            helper(i + 1, prev)
            prev.pop()

            helper(i + 1, prev)

        helper(1, [])
        return result
# @lc code=end
