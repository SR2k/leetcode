#
# @lc app=leetcode.cn id=246 lang=python3
#
# [246] 中心对称数
#
# https://leetcode-cn.com/problems/strobogrammatic-number/description/
#
# algorithms
# Easy (47.71%)
# Likes:    36
# Dislikes: 0
# Total Accepted:    6.3K
# Total Submissions: 13.2K
# Testcase Example:  '"69"'
#
# 中心对称数是指一个数字在旋转了 180 度之后看起来依旧相同的数字（或者上下颠倒地看）。
# 
# 请写一个函数来判断该数字是否是中心对称数，其输入将会以一个字符串的形式来表达数字。
# 
# 
# 
# 示例 1:
# 
# 输入: num = "69"
# 输出: true
# 
# 
# 示例 2:
# 
# 输入: num = "88"
# 输出: true
# 
# 示例 3:
# 
# 输入: num = "962"
# 输出: false
# 
# 示例 4：
# 
# 输入：num = "1"
# 输出：true
# 
# 
#

# @lc code=start
from math import ceil


map = {
    '8': '8',
    '6': '9',
    '9': '6',
    '0': '0',
    '1': '1',
}


class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        for i in range(ceil(len(num) / 2)):
            if num[i] not in map:
                return False
            if map[num[i]] != num[-i - 1]:
                return False

        return True
# @lc code=end
