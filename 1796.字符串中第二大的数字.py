#
# @lc app=leetcode.cn id=1796 lang=python3
#
# [1796] 字符串中第二大的数字
#
# https://leetcode-cn.com/problems/second-largest-digit-in-a-string/description/
#
# algorithms
# Easy (48.29%)
# Likes:    2
# Dislikes: 0
# Total Accepted:    5.5K
# Total Submissions: 11.4K
# Testcase Example:  '"dfa12321afd"'
#
# 给你一个混合字符串 s ，请你返回 s 中 第二大 的数字，如果不存在第二大的数字，请你返回 -1 。
# 
# 混合字符串 由小写英文字母和数字组成。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：s = "dfa12321afd"
# 输出：2
# 解释：出现在 s 中的数字包括 [1, 2, 3] 。第二大的数字是 2 。
# 
# 
# 示例 2：
# 
# 
# 输入：s = "abc1111"
# 输出：-1
# 解释：出现在 s 中的数字只包含 [1] 。没有第二大的数字。
# 
# 
# 
# 
# 提示：
# 
# 
# 1 
# s 只包含小写英文字母和（或）数字。
# 
# 
#

# @lc code=start
class Solution:
    def secondHighest(self, s: str) -> int:
        m1, m2 = -1, -1

        for char in s:
            if not char.isdigit():
                continue
            i = int(char)

            if i > m1:
                m1, m2 = i, m1
            elif m1 > i > m2:
                m2 = i

        return m2
# @lc code=end

