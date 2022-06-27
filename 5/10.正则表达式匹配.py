#
# @lc app=leetcode.cn id=10 lang=python3
#
# [10] 正则表达式匹配
#
# https://leetcode.cn/problems/regular-expression-matching/description/
#
# algorithms
# Hard (31.63%)
# Likes:    3020
# Dislikes: 0
# Total Accepted:    282.1K
# Total Submissions: 891.5K
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
# 输入：s = "aa", p = "a"
# 输出：false
# 解释："a" 无法匹配 "aa" 整个字符串。
# 
# 
# 示例 2:
# 
# 
# 输入：s = "aa", p = "a*"
# 输出：true
# 解释：因为 '*' 代表可以匹配零个或多个前面的那一个元素, 在这里前面的元素就是 'a'。因此，字符串 "aa" 可被视为 'a' 重复了一次。
# 
# 
# 示例 3：
# 
# 
# 输入：s = "ab", p = ".*"
# 输出：true
# 解释：".*" 表示可匹配零个或多个（'*'）任意字符（'.'）。
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= s.length <= 20
# 1 <= p.length <= 30
# s 只包含从 a-z 的小写字母。
# p 只包含从 a-z 的小写字母，以及字符 . 和 *。
# 保证每次出现字符 * 时，前面都匹配到有效的字符
# 
# 
#

# @lc code=start
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        len_s, len_p = len(s), len(p)
        dp = [[False for _ in range(len_p + 1)] for _ in range(len_s + 1)]
        dp[0][0] = True

        for i in range(len_s + 1):
            for j in range(1, len_p + 1):
                char_p = p[j - 1]

                if i == 0:
                    dp[i][j] = char_p == '*' and dp[i][j - 2]
                    continue

                char_s = s[i - 1]

                if char_p == '*':
                    dp[i][j] = dp[i][j - 2] or \
                        (dp[i - 1][j] and Solution.check(char_s, p[j - 2]))
                else:
                    dp[i][j] = dp[i - 1][j - 1] and Solution.check(char_s, char_p)

        return dp[-1][-1]


    @staticmethod
    def check(a: str, b: str):
        if b == '.':
            return True
        return a == b
# @lc code=end

print(Solution().isMatch("aa", "a*"))
