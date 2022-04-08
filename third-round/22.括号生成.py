#
# @lc app=leetcode.cn id=22 lang=python3
#
# [22] 括号生成
#
# https://leetcode-cn.com/problems/generate-parentheses/description/
#
# algorithms
# Medium (77.38%)
# Likes:    2497
# Dislikes: 0
# Total Accepted:    464.4K
# Total Submissions: 600.3K
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
            if len(curr) == n * 2:
                if open_cnt == 0:
                    result.append("".join(curr))
                return

            if open_cnt:
                curr.append(')')
                helper(curr, open_cnt - 1)
                curr.pop()

            if 2 * n - len(curr) >= 2:
                curr.append('(')
                helper(curr, open_cnt + 1)
                curr.pop()

        helper([], 0)
        return result
# @lc code=end

s = Solution()
print(s.generateParenthesis(1))
print(s.generateParenthesis(2))
print(s.generateParenthesis(3))
print(s.generateParenthesis(4))
print(s.generateParenthesis(5))
print(s.generateParenthesis(6))
