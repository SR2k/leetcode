#
# @lc app=leetcode.cn id=680 lang=python3
#
# [680] 验证回文字符串 Ⅱ
#
# https://leetcode-cn.com/problems/valid-palindrome-ii/description/
#
# algorithms
# Easy (40.17%)
# Likes:    358
# Dislikes: 0
# Total Accepted:    75.5K
# Total Submissions: 187.9K
# Testcase Example:  '"aba"'
#
# 给定一个非空字符串 s，最多删除一个字符。判断是否能成为回文字符串。
# 
# 示例 1:
# 
# 
# 输入: "aba"
# 输出: True
# 
# 
# 示例 2:
# 
# 
# 输入: "abca"
# 输出: True
# 解释: 你可以删除c字符。
# 
# 
# 注意:
# 
# 
# 字符串只包含从 a-z 的小写字母。字符串的最大长度是50000。
# 
# 
#

# @lc code=start
class Solution:
    def validPalindrome(self, s: str, left = -1, right = -1, o = 1) -> bool:
        left = 0 if left < 0 else left
        right = len(s) - 1 if right < 0 else right
        length = right - left + 1

        if length <= 1: return True
        if length == 2:
            if s[left] != s[right]: return o >= 1
            return True

        while left <= right:
            if s[left] != s[right]:
                if o == 0: return False
                return self.validPalindrome(s, left + 1, right, 0) or self.validPalindrome(s, left, right - 1, 0)
            else:
                left += 1
                right -= 1

        return True
# @lc code=end

