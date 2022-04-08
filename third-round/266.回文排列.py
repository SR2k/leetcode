#
# @lc app=leetcode.cn id=266 lang=python3
#
# [266] 回文排列
#
# https://leetcode-cn.com/problems/palindrome-permutation/description/
#
# algorithms
# Easy (68.75%)
# Likes:    59
# Dislikes: 0
# Total Accepted:    8.2K
# Total Submissions: 12K
# Testcase Example:  '"code"'
#
# 给定一个字符串，判断该字符串中是否可以通过重新排列组合，形成一个回文字符串。
# 
# 示例 1：
# 
# 输入: "code"
# 输出: false
# 
# 示例 2：
# 
# 输入: "aab"
# 输出: true
# 
# 示例 3：
# 
# 输入: "carerac"
# 输出: true
# 
#

# @lc code=start
class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        single = set()
        for char in s:
            if char in single:
                single.remove(char)
            else:
                single.add(char)
        return len(single) <= 1
# @lc code=end
