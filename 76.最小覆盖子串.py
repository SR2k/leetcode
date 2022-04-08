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
        counter = {}
        for char in t:
            counter[char] = (counter.get(char) or 0) + 1
        lack_cnt = len(counter)

        ri, rj = -1, len(s)
        i = 0
        for j in range(len(s)):
            if s[j] not in counter:
                continue

            counter[s[j]] -= 1
            if counter[s[j]] == 0:
                lack_cnt -= 1

            while Solution.can_remove(counter, s[i]):
                if s[i] in counter:
                    counter[s[i]] += 1
                    if counter[s[i]] == 1:
                        lack_cnt += 1
                i += 1

            if lack_cnt == 0 and rj - ri > j - i:
                ri, rj = i, j

        if ri >= 0:
            return s[ri:rj + 1]
        return ''


    @staticmethod
    def can_remove(counter: Counter, char: str):
        if char not in counter:
            return True
        return counter[char] < 0
# @lc code=end

s = Solution()
print(s.minWindow("ADOBECODEBANC", t = "ABC"))
print(s.minWindow( "a", t = "a"))
print(s.minWindow("a", t = "aa"))

#       |
# ADOBECODEBANC
# |
# ABC
