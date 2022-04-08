#
# @lc app=leetcode.cn id=22 lang=python3
#
# [22] 括号生成
#
# https://leetcode-cn.com/problems/generate-parentheses/description/
#
# algorithms
# Medium (77.36%)
# Likes:    2532
# Dislikes: 0
# Total Accepted:    473.8K
# Total Submissions: 612.4K
# Testcase Example:  '3'
#
# 数字 n 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 有效的 括号组合。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：n = 3
# 输出：["((()))","(()())","(())()","()(())","()()()"]
# 
# 
# 示例 2：
# 
# 
# 输入：n = 1
# 输出：["()"]
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= n <= 8
# 
# 
#

# @lc code=start
class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        result = []

        def helper(curr: list[str], open: int):
            if len(curr) == n * 2:
                result.append(''.join(curr))
                return

            if 2 * n - len(curr) > open:
                curr.append('(')
                helper(curr, open + 1)
                curr.pop()

            if open:
                curr.append(')')
                helper(curr, open - 1)
                curr.pop()

        helper([], 0)
        return result
# @lc code=end
