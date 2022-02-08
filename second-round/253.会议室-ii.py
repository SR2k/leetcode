#
# @lc app=leetcode.cn id=253 lang=python3
#
# [253] 会议室 II
#
# https://leetcode-cn.com/problems/meeting-rooms-ii/description/
#
# algorithms
# Medium (50.65%)
# Likes:    377
# Dislikes: 0
# Total Accepted:    37.7K
# Total Submissions: 74.5K
# Testcase Example:  '[[0,30],[5,10],[15,20]]'
#
# 给你一个会议时间安排的数组 intervals ，每个会议时间都会包括开始和结束的时间 intervals[i] = [starti, endi]
# ，为避免会议冲突，同时要考虑充分利用会议室资源，请你计算至少需要多少间会议室，才能满足这些会议安排。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：intervals = [[0,30],[5,10],[15,20]]
# 输出：2
# 
# 
# 示例 2：
# 
# 
# 输入：intervals = [[7,10],[2,4]]
# 输出：1
# 
# 
# 
# 
# 提示：
# 
# 
# 1 
# 0 i < endi 
# 
# 
#

# @lc code=start
class Solution:
    def minMeetingRooms(self, intervals: list[list[int]]) -> int:
        d = []
        for begin, end in intervals:
            d.append((begin, 1))
            d.append((end, -1))
        d.sort()

        result = 0
        curr = 0
        for _, delta in d:
            curr += delta
            result = max(result, curr)
        return result
# @lc code=end

