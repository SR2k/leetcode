#
# @lc app=leetcode.cn id=22 lang=python3
#
# [22] 括号生成
#
# https://leetcode-cn.com/problems/generate-parentheses/description/
#
# algorithms
# Medium (77.30%)
# Likes:    2297
# Dislikes: 0
# Total Accepted:    407.2K
# Total Submissions: 526.8K
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
        c = [[''], ['()']]

        for i in range(2, n + 1):
            t = []
            for a in range(i):
                b = i - a - 1

                for pa in c[a]:
                    for pb in c[b]:
                        t.append(f"({pa}){pb}")

            c.append(t)

        return c[n]
# @lc code=end

s = Solution()
print(s.generateParenthesis(0))
print(s.generateParenthesis(1))
print(s.generateParenthesis(2))
print(s.generateParenthesis(3))
