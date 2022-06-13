#
# @lc app=leetcode.cn id=76 lang=python3
#
# [76] 最小覆盖子串
#
# https://leetcode.cn/problems/minimum-window-substring/description/
#
# algorithms
# Hard (44.23%)
# Likes:    1923
# Dislikes: 0
# Total Accepted:    295.3K
# Total Submissions: 667.7K
# Testcase Example:  '"ADOBECODEBANC"\n"ABC"'
#
# 给你一个字符串 s 、一个字符串 t 。返回 s 中涵盖 t 所有字符的最小子串。如果 s 中不存在涵盖 t 所有字符的子串，则返回空字符串 ""
# 。
# 
# 
# 
# 注意：
# 
# 
# 对于 t 中重复字符，我们寻找的子字符串中该字符数量必须不少于 t 中该字符数量。
# 如果 s 中存在这样的子串，我们保证它是唯一的答案。
# 
# 
# 
# 
# 示例 1：
# 
# 
# 输入：s = "ADOBECODEBANC", t = "ABC"
# 输出："BANC"
# 
# 
# 示例 2：
# 
# 
# 输入：s = "a", t = "a"
# 输出："a"
# 
# 
# 示例 3:
# 
# 
# 输入: s = "a", t = "aa"
# 输出: ""
# 解释: t 中两个字符 'a' 均应包含在 s 的子串中，
# 因此没有符合条件的子字符串，返回空字符串。
# 
# 
# 
# 提示：
# 
# 
# 1 
# s 和 t 由英文字母组成
# 
# 
# 
# 进阶：你能设计一个在 o(n) 时间内解决此问题的算法吗？
#

# @lc code=start
from collections import Counter


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ''

        extra = Counter(t)
        keys = set(extra.keys())
        extra_count = len(keys)

        result = [-1, float('inf')]

        begin = 0
        for end in range(len(s)):
            char = s[end]

            if char not in keys:
                continue

            extra[char] -= 1
            if extra[char] == 0:
                extra_count -= 1

            while Solution.can_remove(extra, keys, s[begin]):
                extra[s[begin]] += 1
                begin += 1

            if extra_count == 0 and end - begin < result[1] - result[0]:
                result = [begin, end]

        if result[0] < 0:
            return ''
        return s[result[0]:result[1] + 1]


    def can_remove(extra: Counter, keys: set, char: str):
        return char not in keys or extra[char] < 0
# @lc code=end

print(Solution().minWindow("ADOBECODEBANC", "ABC"))
print(Solution().minWindow("ADOBC", "ABC"))
print(Solution().minWindow("ZZZADOBC", "ABC"))
print(Solution().minWindow("ADOBCZZZ", "ABC"))
print(Solution().minWindow("a", "a"))
