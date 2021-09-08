#
# @lc app=leetcode.cn id=539 lang=python3
#
# [539] 最小时间差
#
# https://leetcode-cn.com/problems/minimum-time-difference/description/
#
# algorithms
# Medium (59.52%)
# Likes:    98
# Dislikes: 0
# Total Accepted:    13.6K
# Total Submissions: 22.8K
# Testcase Example:  '["23:59","00:00"]'
#
# 给定一个 24 小时制（小时:分钟 "HH:MM"）的时间列表，找出列表中任意两个时间的最小时间差并以分钟数表示。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：timePoints = ["23:59","00:00"]
# 输出：1
# 
# 
# 示例 2：
# 
# 
# 输入：timePoints = ["00:00","23:59","00:00"]
# 输出：0
# 
# 
# 
# 
# 提示：
# 
# 
# 2 
# timePoints[i] 格式为 "HH:MM"
# 
# 
#

# @lc code=start
def convert(a):
    return int(a[:2]) * 60 + int(a[3:5])


def substract(a, b):
    result = a - b
    return result if result >= 0 else 24 * 60 + result


class Solution:
    def findMinDifference(self, timePoints: list[str]) -> int:
        time_list = sorted(map(convert, timePoints))

        result = float('inf')
        for i in range(len(time_list)):
            result = min(substract(time_list[i], time_list[i - 1]), result)

            if result == 0:
                return result

        return result
# @lc code=end
