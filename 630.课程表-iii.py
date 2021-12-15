#
# @lc app=leetcode.cn id=630 lang=python3
#
# [630] 课程表 III
#
# https://leetcode-cn.com/problems/course-schedule-iii/description/
#
# algorithms
# Hard (37.22%)
# Likes:    219
# Dislikes: 0
# Total Accepted:    9.9K
# Total Submissions: 24.4K
# Testcase Example:  '[[100,200],[200,1300],[1000,1250],[2000,3200]]'
#
# 这里有 n 门不同的在线课程，按从 1 到 n 编号。给你一个数组 courses ，其中 courses[i] = [durationi,
# lastDayi] 表示第 i 门课将会 持续 上 durationi 天课，并且必须在不晚于 lastDayi 的时候完成。
# 
# 你的学期从第 1 天开始。且不能同时修读两门及两门以上的课程。
# 
# 返回你最多可以修读的课程数目。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：courses = [[100, 200], [200, 1300], [1000, 1250], [2000, 3200]]
# 输出：3
# 解释：
# 这里一共有 4 门课程，但是你最多可以修 3 门：
# 首先，修第 1 门课，耗费 100 天，在第 100 天完成，在第 101 天开始下门课。
# 第二，修第 3 门课，耗费 1000 天，在第 1100 天完成，在第 1101 天开始下门课程。
# 第三，修第 2 门课，耗时 200 天，在第 1300 天完成。
# 第 4 门课现在不能修，因为将会在第 3300 天完成它，这已经超出了关闭日期。
# 
# 示例 2：
# 
# 
# 输入：courses = [[1,2]]
# 输出：1
# 
# 
# 示例 3：
# 
# 
# 输入：courses = [[3,2],[4,3]]
# 输出：0
# 
# 
# 
# 
# 提示:
# 
# 
# 1 <= courses.length <= 10^4
# 1 <= durationi, lastDayi <= 10^4
# 
# 
#

# @lc code=start
from heapq import heappop, heappush


class Solution:
    def scheduleCourse(self, courses: list[list[int]]) -> int:
        curr_date = 1
        courses.sort(key=lambda x: x[1])
        result_queue = []

        for duration, end_date in courses:
            heappush(result_queue, (-duration, end_date))

            if curr_date + duration - 1 > end_date:
                d, _ = heappop(result_queue)
                curr_date -= -d

            curr_date += duration

        return len(result_queue)
# @lc code=end

s = Solution()
print(s.scheduleCourse(courses = [[100, 200], [200, 1300], [1000, 1250], [2000, 3200]]))
print(s.scheduleCourse(courses = [[1,2]]))
print(s.scheduleCourse(courses = [[3,2],[4,3]]))
print(s.scheduleCourse([[7,16],[2,3],[3,12],[3,14],[10,19],[10,16],[6,8],[6,11],[3,13],[6,16]]))
print(s.scheduleCourse([[5,5],[4,6],[2,6]]))
print(s.scheduleCourse([[5,15],[3,19],[6,7],[2,10],[5,16],[8,14],[10,11],[2,19]]))
