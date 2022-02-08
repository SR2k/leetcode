#
# @lc app=leetcode.cn id=10 lang=python3
#
# [10] 正则表达式匹配
#
# https://leetcode-cn.com/problems/regular-expression-matching/description/
#
# algorithms
# Hard (31.65%)
# Likes:    2656
# Dislikes: 0
# Total Accepted:    230.6K
# Total Submissions: 728.7K
# Testcase Example:  '"aa"\n"a"'
#
# 给你一个字符串 s 和一个字符规律 p，请你来实现一个支持 '.' 和 '*' 的正则表达式匹配。
# 
# 
# '.' 匹配任意单个字符
# '*' 匹配零个或多个前面的那一个元素
# 
# 
# 所谓匹配，是要涵盖 整个 字符串 s的，而不是部分字符串。
# 
# 
# 示例 1：
# 
# 
# 输入：s = "aa" p = "a"
# 输出：false
# 解释："a" 无法匹配 "aa" 整个字符串。
# 
# 
# 示例 2:
# 
# 
# 输入：s = "aa" p = "a*"
# 输出：true
# 解释：因为 '*' 代表可以匹配零个或多个前面的那一个元素, 在这里前面的元素就是 'a'。因此，字符串 "aa" 可被视为 'a' 重复了一次。
# 
# 
# 示例 3：
# 
# 
# 输入：s = "ab" p = ".*"
# 输出：true
# 解释：".*" 表示可匹配零个或多个（'*'）任意字符（'.'）。
# 
# 
# 示例 4：
# 
# 
# 输入：s = "aab" p = "c*a*b"
# 输出：true
# 解释：因为 '*' 表示零个或多个，这里 'c' 为 0 个, 'a' 被重复一次。因此可以匹配字符串 "aab"。
# 
# 
# 示例 5：
# 
# 
# 输入：s = "mississippi" p = "mis*is*p*."
# 输出：false
# 
# 
# 
# 提示：
# 
# 
# 1 <= s.length <= 20
# 1 <= p.length <= 30
# s 只含小写英文字母。
# p 只含小写英文字母，以及字符 . 和 *。
# 保证每次出现字符 * 时，前面都匹配到有效的字符
# 
# 
#

# @lc code=start
class Solution:
    @staticmethod
    def match_single(a: str, b: str):
        # print('match single::', a, b)
        if b == '.':
            return len(a) == 1
        return a == b

    @staticmethod
    def match_star(a: str, b_pre: str):
        # print('match star::', a, b_pre)
        if b_pre == '.':
            return True
        return a == len(a) * b_pre

    def isMatch(self, s: str, p: str) -> bool:
        # 前 i 个字符与前 p 个字符是否匹配
        dp = [[False for _ in range(len(p) + 1)] for __ in range(len(s) + 1)]

        for i in range(len(s) + 1):
            for j in range(len(p) + 1):
                if j == 0:
                    dp[i][j] = i == 0

                elif p[j - 1] == '*':
                    if j == 1:
                        dp[i][j] = Solution.match_star(s[:i], p[j - 2])
                    elif s[i - 1] == p[j - 2] or p[j - 2] == '.': # can match
                        dp[i][j] = dp[i][j - 2] or dp[i - 1][j]
                    else: # cannot match
                        dp[i][j] = dp[i][j - 2]

                else:
                    if j == 0:
                        dp[i][j] = Solution.match_single(s[:i], p[j - 1])
                    else:
                        dp[i][j] = dp[i - 1][j - 1] and Solution.match_single(s[i - 1], p[j - 1])

        # print(dp)
        return dp[-1][-1]
# @lc code=end

s = Solution()
print(s.isMatch(s = "aa", p = "a"))
print(s.isMatch(s = "aa", p = "a*"))
print(s.isMatch(s = "ab", p = ".*"))
print(s.isMatch(s = "aab", p = "c*a*b"))
print(s.isMatch(s = "mississippi", p = "mis*is*p*.")) # False
print(s.isMatch("mississippi", "mis*is*ip*.")) # True
