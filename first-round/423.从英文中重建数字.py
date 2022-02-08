#
# @lc app=leetcode.cn id=423 lang=python3
#
# [423] 从英文中重建数字
#
# https://leetcode-cn.com/problems/reconstruct-original-digits-from-english/description/
#
# algorithms
# Medium (57.03%)
# Likes:    134
# Dislikes: 0
# Total Accepted:    22.6K
# Total Submissions: 37.3K
# Testcase Example:  '"owoztneoer"'
#
# 给你一个字符串 s ，其中包含字母顺序打乱的用英文单词表示的若干数字（0-9）。按 升序 返回原始的数字。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：s = "owoztneoer"
# 输出："012"
# 
# 
# 示例 2：
# 
# 
# 输入：s = "fviefuro"
# 输出："45"
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= s.length <= 10^5
# s[i] 为 ["e","g","f","i","h","o","n","s","r","u","t","w","v","x","z"]
# 这些字符之一
# s 保证是一个符合题目要求的字符串
# 
# 
#

# @lc code=start
from collections import Counter
class Solution:
    def originalDigits(self, s: str) -> str:
        counter = Counter(s)
        c0 = counter['z']
        c2 = counter['w']
        c4 = counter['u']
        c5 = counter['f'] - c4
        c6 = counter['x']
        c7 = counter['s'] - c6
        c8 = counter['g']
        c3 = counter['h'] - c8
        c1 = counter['o'] - c0 - c2 - c4
        c9 = counter['i'] - c5 - c6 - c8

        return "0" * c0 + \
            "1" * c1 + \
            "2" * c2 + \
            "3" * c3 + \
            "4" * c4 + \
            "5" * c5 + \
            "6" * c6 + \
            "7" * c7 + \
            "8" * c8 + \
            "9" * c9
# @lc code=end

