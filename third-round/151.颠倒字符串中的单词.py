#
# @lc app=leetcode.cn id=151 lang=python3
#
# [151] 翻转字符串里的单词
#
# https://leetcode-cn.com/problems/reverse-words-in-a-string/description/
#
# algorithms
# Medium (49.65%)
# Likes:    491
# Dislikes: 0
# Total Accepted:    225.9K
# Total Submissions: 453.4K
# Testcase Example:  '"the sky is blue"'
#
# 给你一个字符串 s ，颠倒字符串中 单词 的顺序。
# 
# 单词 是由非空格字符组成的字符串。s 中使用至少一个空格将字符串中的 单词 分隔开。
# 
# 返回 单词 顺序颠倒且 单词 之间用单个空格连接的结果字符串。
# 
# 注意：输入字符串 s中可能会存在前导空格、尾随空格或者单词间的多个空格。返回的结果字符串中，单词间应当仅用单个空格分隔，且不包含任何额外的空格。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：s = "the sky is blue"
# 输出："blue is sky the"
# 
# 
# 示例 2：
# 
# 
# 输入：s = "  hello world  "
# 输出："world hello"
# 解释：颠倒后的字符串中不能存在前导空格和尾随空格。
# 
# 
# 示例 3：
# 
# 
# 输入：s = "a good   example"
# 输出："example good a"
# 解释：如果两个单词间有多余的空格，颠倒后的字符串需要将单词间的空格减少到仅有一个。
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= s.length <= 10^4
# s 包含英文大小写字母、数字和空格 ' '
# s 中 至少存在一个 单词
# 
# 
# 
# 
# 
# 
# 
# 进阶：如果字符串在你使用的编程语言中是一种可变数据类型，请尝试使用 O(1) 额外空间复杂度的 原地 解法。
# 
#

# @lc code=start
class Solution:
    def reverseWords(self, s: str) -> str:
        s = list(s)
        s = Solution.remove_spaces(s)
        Solution.reverse(s)

        i = 0
        while i < len(s):
            j = i
            while j + 1 < len(s) and s[j + 1] != ' ':
                j += 1
            Solution.reverse(s, i, j)
            i = j + 2

        # print(s)
        return "".join(s)


    @staticmethod
    def reverse(s: list[str], i = None, j = None):
        i = 0 if i is None else i
        j = len(s) - 1 if j is None else j

        while i < j:
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1


    @staticmethod
    def remove_spaces(s: list[str]) -> list[str]:
        p = i = 0
        while i < len(s) and s[i] == ' ':
            i += 1
        if i == len(s):
            return []

        while i < len(s):
            while i < len(s) and s[i] == ' ':
                i += 1
            if i == len(s):
                break

            if p != 0:
                s[p] = ' '
                p += 1

            while i < len(s) and s[i] != ' ':
                s[p] = s[i]
                p += 1
                i += 1

        while len(s) > p:
            s.pop()

        return s
# @lc code=end

s = Solution()
print(s.reverseWords( "    a  "))
print(s.reverseWords( "a"))
print(s.reverseWords( "the sky is blue"))
print(s.reverseWords("  hello world  "))
print(s.reverseWords("a good  example"))
print(s.reverseWords(" a good     example    "))
