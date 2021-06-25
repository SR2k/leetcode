#
# @lc app=leetcode.cn id=186 lang=python3
#
# [186] 翻转字符串里的单词 II
#
# https://leetcode-cn.com/problems/reverse-words-in-a-string-ii/description/
#
# algorithms
# Medium (74.82%)
# Likes:    57
# Dislikes: 0
# Total Accepted:    6.6K
# Total Submissions: 8.8K
# Testcase Example:  '["t","h","e"," ","s","k","y"," ","i","s"," ","b","l","u","e"]'
#
# 给定一个字符串，逐个翻转字符串中的每个单词。
# 
# 示例：
# 
# 输入: ["t","h","e"," ","s","k","y"," ","i","s"," ","b","l","u","e"]
# 输出: ["b","l","u","e"," ","i","s"," ","s","k","y"," ","t","h","e"]
# 
# 注意：
# 
# 
# 单词的定义是不包含空格的一系列字符
# 输入字符串中不会包含前置或尾随的空格
# 单词与单词之间永远是以单个空格隔开的
# 
# 
# 进阶：使用 O(1) 额外空间复杂度的原地解法。
# 
#

# @lc code=start
class Solution:
    def reverseWords(self, s: list[str]) -> None:
        s.reverse()

        left, right = 0, 0
        while right < len(s):
            while right + 1 < len(s) and s[right + 1].isalnum():
                right += 1
            next = right + 1

            while left < right:
                s[left], s[right] = s[right], s[left]
                left += 1
                right -= 1

            while next < len(s) and not s[next].isalnum():
                next += 1
            left, right = next, next
# @lc code=end

a = ["t","h","e"," ","s","k","y"," ","i","s"," ","b","l","u","e"]
Solution().reverseWords(a)
print(a)
