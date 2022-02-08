#
# @lc app=leetcode.cn id=1344 lang=python3
#
# [1344] 时钟指针的夹角
#
# https://leetcode-cn.com/problems/angle-between-hands-of-a-clock/description/
#
# algorithms
# Medium (59.84%)
# Likes:    35
# Dislikes: 0
# Total Accepted:    6.8K
# Total Submissions: 11.3K
# Testcase Example:  '12\n30'
#
# 给你两个数 hour 和 minutes 。请你返回在时钟上，由给定时间的时针和分针组成的较小角的角度（60 单位制）。
# 
# 
# 
# 示例 1：
# 
# 
# 
# 输入：hour = 12, minutes = 30
# 输出：165
# 
# 
# 示例 2：
# 
# 
# 
# 输入：hour = 3, minutes = 30
# 输出；75
# 
# 
# 示例 3：
# 
# 
# 
# 输入：hour = 3, minutes = 15
# 输出：7.5
# 
# 
# 示例 4：
# 
# 输入：hour = 4, minutes = 50
# 输出：155
# 
# 
# 示例 5：
# 
# 输入：hour = 12, minutes = 0
# 输出：0
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= hour <= 12
# 0 <= minutes <= 59
# 与标准答案误差在 10^-5 以内的结果都被视为正确结果。
# 
# 
#

# @lc code=start
HOUR_DEGREE = 360 // 12
MINUTE_DEGREE = 360 // 60

class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        hour %= 12
        h = hour * HOUR_DEGREE + HOUR_DEGREE / 60 * minutes
        m = minutes * MINUTE_DEGREE

        r = max(h, m) - min(h, m)
        return 360 - r if r >= 180 else r
# @lc code=end

s = Solution()
print(s.angleClock(hour = 12, minutes = 30))
print(s.angleClock(hour = 3, minutes = 30))
print(s.angleClock(hour = 3, minutes = 15))
print(s.angleClock(hour = 4, minutes = 50))
print(s.angleClock(hour = 12, minutes = 0))
print(s.angleClock(1, 57))
