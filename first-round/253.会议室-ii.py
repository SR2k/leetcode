#
# @lc app=leetcode.cn id=253 lang=python3
#
# [253] 会议室 II
#
# https://leetcode-cn.com/problems/meeting-rooms-ii/description/
#
# algorithms
# Medium (49.18%)
# Likes:    290
# Dislikes: 0
# Total Accepted:    26.8K
# Total Submissions: 54.6K
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
        d: list[tuple[int, int]] = []
        for begin, end in intervals:
            d.append((begin, 1))
            d.append((end, -1))

        # 同一个时间又有开始又有结束的，先结束再开始
        d.sort(key=lambda x: x[0] * 10000 + x[1])

        prev, count, ret = 0, 0, 0
        for time, delta in d:
            count += delta
            if prev != time:
                ret = max(ret, count if delta > 0 else count + 1)
            prev = time

        return max(ret, count)
# @lc code=end

print(Solution().minMeetingRooms([[13,15],[1,13]]))
