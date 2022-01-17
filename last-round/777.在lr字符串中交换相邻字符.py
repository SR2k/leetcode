#
# @lc app=leetcode.cn id=777 lang=python3
#
# [777] 在LR字符串中交换相邻字符
#
# https://leetcode-cn.com/problems/swap-adjacent-in-lr-string/description/
#
# algorithms
# Medium (32.40%)
# Likes:    96
# Dislikes: 0
# Total Accepted:    5.2K
# Total Submissions: 16.1K
# Testcase Example:  '"RXXLRXRXL"\n"XRLXXRRLX"'
#
# 在一个由 'L' , 'R' 和 'X'
# 三个字符组成的字符串（例如"RXXLRXRXL"）中进行移动操作。一次移动操作指用一个"LX"替换一个"XL"，或者用一个"XR"替换一个"RX"。现给定起始字符串start和结束字符串end，请编写代码，当且仅当存在一系列移动操作使得start可以转换成end时，
# 返回True。
# 
# 
# 
# 示例 :
# 
# 输入: start = "RXXLRXRXL", end = "XRLXXRRLX"
# 输出: True
# 解释:
# 我们可以通过以下几步将start转换成end:
# RXXLRXRXL ->
# XRXLRXRXL ->
# XRLXRXRXL ->
# XRLXXRRXL ->
# XRLXXRRLX
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= len(start) = len(end) <= 10000。
# start和end中的字符串仅限于'L', 'R'和'X'。
# 
# 
#

# @lc code=start
class Solution:
    def canTransform(self, start: str, end: str) -> bool:
        len_1, len_2 = len(start), len(end)
        p1, p2 = 0, 0
        c1, c2 = 0, 0

        while True:
            while p1 < len_1 and start[p1] == 'X':
                c1 += 1
                p1 += 1
            while p2 < len_2 and end[p2] == 'X':
                c2 += 1
                p2 += 1

            if p1 >= len_1 or p2 >= len_2:
                break

            if start[p1] != end[p2]:
                return False
            if start[p1] == 'L' and c2 > c1:
                return False
            if start[p1] == 'R' and c1 > c2:
                return False

            p1 += 1
            p2 += 1

        while p1 < len_1:
            if start[p1] == 'X':
                c1 += 1
            else:
                return False
            p1 += 1
        while p2 < len_2:
            if end[p2] == 'X':
                c2 += 1
            else:
                return False
            p2 += 1

        return c1 == c2
# @lc code=end

