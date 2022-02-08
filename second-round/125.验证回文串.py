#
# @lc app=leetcode.cn id=125 lang=python3
#
# [125] 验证回文串
#
# https://leetcode-cn.com/problems/valid-palindrome/description/
#
# algorithms
# Easy (47.12%)
# Likes:    460
# Dislikes: 0
# Total Accepted:    312.6K
# Total Submissions: 663.4K
# Testcase Example:  '"A man, a plan, a canal: Panama"'
#
# 给定一个字符串，验证它是否是回文串，只考虑字母和数字字符，可以忽略字母的大小写。
# 
# 说明：本题中，我们将空字符串定义为有效的回文串。
# 
# 
# 
# 示例 1:
# 
# 
# 输入: "A man, a plan, a canal: Panama"
# 输出: true
# 解释："amanaplanacanalpanama" 是回文串
# 
# 
# 示例 2:
# 
# 
# 输入: "race a car"
# 输出: false
# 解释："raceacar" 不是回文串
# 
# 
# 
# 
# 提示：
# 
# 
# 1 
# 字符串 s 由 ASCII 字符组成
# 
# 
#

# @lc code=start
class Solution:
    def isPalindrome(self, s: str) -> bool:
        i, j = 0, len(s) - 1

        while i < j:
            while i < j and not s[i].isalnum():
                i += 1
            while i < j and not s[j].isalnum():
                j -= 1

            if s[i].lower() != s[j].lower():
                return False

            i += 1
            j -= 1

        return True
# @lc code=end

s = Solution()
# print(s.isPalindrome("A man, a plan, a canal: Panama"))
# print(s.isPalindrome("      A man, a plan, a canal: Panama"))
# print(s.isPalindrome("A   man, a plan, a canal: Panama     "))
# print(s.isPalindrome("race a car"))
print(s.isPalindrome("0P"))
