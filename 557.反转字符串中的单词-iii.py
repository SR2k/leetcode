#
# @lc app=leetcode.cn id=557 lang=python3
#
# [557] 反转字符串中的单词 III
#
# https://leetcode.cn/problems/reverse-words-in-a-string-iii/description/
#
# algorithms
# Easy (74.18%)
# Likes:    446
# Dislikes: 0
# Total Accepted:    241K
# Total Submissions: 324.8K
# Testcase Example:  `"Let's take LeetCode contest"`
#
# 给定一个字符串 s ，你需要反转字符串中每个单词的字符顺序，同时仍保留空格和单词的初始顺序。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：s = "Let's take LeetCode contest"
# 输出："s'teL ekat edoCteeL tsetnoc"
# 
# 
# 示例 2:
# 
# 
# 输入： s = "God Ding"
# 输出："doG gniD"
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= s.length <= 5 * 10^4
# s 包含可打印的 ASCII 字符。
# s 不包含任何开头或结尾空格。
# s 里 至少 有一个词。
# s 中的所有单词都用一个空格隔开。
# 
# 
#

# @lc code=start
class Solution:
    def reverseWords(self, s: str) -> str:
        begin = 0
        s = list(s)

        while begin < len(s):
            end = begin

            while end + 1 < len(s) and s[end + 1] != ' ':
                end += 1

            Solution.reverse(s, begin, end)
            begin = end + 2

        return "".join(s)

    @staticmethod
    def reverse(s: list[str], i: int, j: int):
        while i < j:
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1
# @lc code=end
