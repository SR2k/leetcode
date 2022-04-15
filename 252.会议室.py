#
# @lc app=leetcode.cn id=252 lang=python3
#
# [252] 会议室
#
# https://leetcode-cn.com/problems/meeting-rooms/description/
#
# algorithms
# Easy (57.02%)
# Likes:    117
# Dislikes: 0
# Total Accepted:    16.5K
# Total Submissions: 29K
# Testcase Example:  '[[0,30],[5,10],[15,20]]'
#
# 给定一个会议时间安排的数组 intervals ，每个会议时间都会包括开始和结束的时间 intervals[i] = [starti, endi]
# ，请你判断一个人是否能够参加这里面的全部会议。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：intervals = [[0,30],[5,10],[15,20]]
# 输出：false
# 
# 
# 示例 2：
# 
# 
# 输入：intervals = [[7,10],[2,4]]
# 输出：true
# 
# 
# 
# 
# 提示：
# 
# 
# 0 
# intervals[i].length == 2
# 0 i i 
# 
# 
#

# @lc code=start
class Solution:
    def canAttendMeetings(self, intervals: list[list[int]]) -> bool:
        intervals.sort()

        for i, interval in enumerate(intervals):
            if i == 0:
                continue
            if interval[0] < intervals[i - 1][1]:
                return False

        return True
# @lc code=end

