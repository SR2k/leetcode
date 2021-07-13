#
# @lc app=leetcode.cn id=709 lang=python3
#
# [709] 转换成小写字母
#
# https://leetcode-cn.com/problems/to-lower-case/description/
#
# algorithms
# Easy (76.09%)
# Likes:    151
# Dislikes: 0
# Total Accepted:    68K
# Total Submissions: 89.4K
# Testcase Example:  '"Hello"'
#
# 给你一个字符串 s ，将该字符串中的大写字母转换成相同的小写字母，返回新的字符串。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：s = "Hello"
# 输出："hello"
# 
# 
# 示例 2：
# 
# 
# 输入：s = "here"
# 输出："here"
# 
# 
# 示例 3：
# 
# 
# 输入：s = "LOVELY"
# 输出："lovely"
# 
# 
# 
# 
# 提示：
# 
# 
# 1 
# s 由 ASCII 字符集中的可打印字符组成
# 
# 
#

# @lc code=start
ORD_A, ORD_BIG_A, ORD_BIG_Z = ord('a'), ord('A'), ord('Z')
DELTA = ORD_A - ORD_BIG_A


class Solution:
    def toLowerCase(self, s: str) -> str:
        ret = ''

        for char in s:
            o = ord(char)
            if ORD_BIG_A <= o <= ORD_BIG_Z:
                ret += chr(DELTA + o)
            else:
                ret += char

        return ret

# @lc code=end

