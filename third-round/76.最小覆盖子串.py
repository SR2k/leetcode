#
# @lc app=leetcode.cn id=76 lang=python3
#
# [76] 最小覆盖子串
#
# https://leetcode-cn.com/problems/minimum-window-substring/description/
#
# algorithms
# Hard (43.48%)
# Likes:    1701
# Dislikes: 0
# Total Accepted:    247.8K
# Total Submissions: 568.1K
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
            return ""

        required = Counter(t)
        required_cnt = len(required.keys())

        def can_move(i: int):
            if s[i] not in required:
                return True
            return required[s[i]] + 1 <= 0

        i = 0
        l, r = -1, len(s) + 1
        for j in range(len(s)):
            if s[j] in required:
                required[s[j]] -= 1
                if required[s[j]] == 0:
                    required_cnt -= 1

            while i < j and can_move(i):
                if s[i] in required:
                    required[s[i]] += 1
                    if required[s[i]] == 1:
                        required_cnt += 1
                i += 1

            # print(i, j, required_cnt)

            if required_cnt == 0 and r - l > j - i:
                l, r = i, j

        return s[l:r + 1] if l >= 0 else ""
# @lc code=end

s = Solution()
print(s.minWindow("a", "b"))
print(s.minWindow("ADOBECODEBANC", t = "ABC"))
print(s.minWindow("ab", "a"))
print(s.minWindow("ab", "b"))
print(s.minWindow("a", t = "a"))
print(s.minWindow("a", t = "aa"))
