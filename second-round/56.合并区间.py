#
# @lc app=leetcode.cn id=56 lang=python3
#
# [56] 合并区间
#
# https://leetcode-cn.com/problems/merge-intervals/description/
#
# algorithms
# Medium (47.62%)
# Likes:    1269
# Dislikes: 0
# Total Accepted:    352.9K
# Total Submissions: 740.8K
# Testcase Example:  '[[1,3],[2,6],[8,10],[15,18]]'
#
# 以数组 intervals 表示若干个区间的集合，其中单个区间为 intervals[i] = [starti, endi]
# 。请你合并所有重叠的区间，并返回一个不重叠的区间数组，该数组需恰好覆盖输入中的所有区间。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：intervals = [[1,3],[2,6],[8,10],[15,18]]
# 输出：[[1,6],[8,10],[15,18]]
# 解释：区间 [1,3] 和 [2,6] 重叠, 将它们合并为 [1,6].
# 
# 
# 示例 2：
# 
# 
# 输入：intervals = [[1,4],[4,5]]
# 输出：[[1,5]]
# 解释：区间 [1,4] 和 [4,5] 可被视为重叠区间。
# 
# 
# 
# 提示：
# 
# 
# 1 
# intervals[i].length == 2
# 0 i i 
# 
# 
#


from typing import List


# @lc code=start
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        result = []

        for begin, end in intervals:
            if not result or result[-1][1] < begin:
                result.append([begin, end])
            else:
                result[-1][1] = max(result[-1][1], end)

        return result
# @lc code=end

s = Solution()
print(s.merge([[1,3],[2,6],[8,10],[15,18]]))
print(s.merge([[1,4],[4,5]]))
