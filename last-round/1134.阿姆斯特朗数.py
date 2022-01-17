#
# @lc app=leetcode.cn id=1134 lang=python3
#
# [1134] 阿姆斯特朗数
#
# https://leetcode-cn.com/problems/armstrong-number/description/
#
# algorithms
# Easy (77.20%)
# Likes:    8
# Dislikes: 0
# Total Accepted:    3K
# Total Submissions: 3.9K
# Testcase Example:  '153'
#
# 假设存在一个 k 位数 N，其每一位上的数字的 k 次幂的总和也是 N，那么这个数是阿姆斯特朗数。
# 
# 给你一个正整数 N，让你来判定他是否是阿姆斯特朗数，是则返回 true，不是则返回 false。
# 
# 
# 
# 示例 1：
# 
# 输入：153
# 输出：true
# 示例： 
# 153 是一个 3 位数，且 153 = 1^3 + 5^3 + 3^3。
# 
# 
# 示例 2：
# 
# 输入：123
# 输出：false
# 解释： 
# 123 是一个 3 位数，且 123 != 1^3 + 2^3 + 3^3 = 36。
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= N <= 10^8
# 
# 
#

# @lc code=start
class Solution:
    def isArmstrong(self, n: int) -> bool:
        t, x = [], n

        while x:
            t.append(x % 10)
            x //= 10

        k = len(t)
        return sum([i ** k for i in t]) == n
# @lc code=end

