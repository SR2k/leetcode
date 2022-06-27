#
# @lc app=leetcode.cn id=22 lang=python3
#
# [22] 括号生成
#
# https://leetcode.cn/problems/generate-parentheses/description/
#
# algorithms
# Medium (77.45%)
# Likes:    2626
# Dislikes: 0
# Total Accepted:    500.7K
# Total Submissions: 646.5K
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


        def helper(curr: list[str], open_cnt: int):
            if (len(curr) == 2 * n) and not open_cnt:
                result.append(''.join(curr))
                return

            # can open
            if len(curr) + open_cnt + 2 <= 2 * n:
                curr.append('(')
                helper(curr, open_cnt + 1)
                curr.pop()

            # can close
            if open_cnt > 0:
                curr.append(')')
                helper(curr, open_cnt - 1)
                curr.pop()


        helper([], 0)
        return result
# @lc code=end
