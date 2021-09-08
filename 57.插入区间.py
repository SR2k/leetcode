#
# @lc app=leetcode.cn id=57 lang=python3
#
# [57] 插入区间
#
# https://leetcode-cn.com/problems/insert-interval/description/
#
# algorithms
# Medium (41.08%)
# Likes:    477
# Dislikes: 0
# Total Accepted:    84.5K
# Total Submissions: 205.8K
# Testcase Example:  '[[1,3],[6,9]]\n[2,5]'
#
# 给你一个 无重叠的 ，按照区间起始端点排序的区间列表。
# 
# 在列表中插入一个新的区间，你需要确保列表中的区间仍然有序且不重叠（如果有必要的话，可以合并区间）。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：intervals = [[1,3],[6,9]], newInterval = [2,5]
# 输出：[[1,5],[6,9]]
# 
# 
# 示例 2：
# 
# 
# 输入：intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
# 输出：[[1,2],[3,10],[12,16]]
# 解释：这是因为新的区间 [4,8] 与 [3,5],[6,7],[8,10] 重叠。
# 
# 示例 3：
# 
# 
# 输入：intervals = [], newInterval = [5,7]
# 输出：[[5,7]]
# 
# 
# 示例 4：
# 
# 
# 输入：intervals = [[1,5]], newInterval = [2,3]
# 输出：[[1,5]]
# 
# 
# 示例 5：
# 
# 
# 输入：intervals = [[1,5]], newInterval = [2,7]
# 输出：[[1,7]]
# 
# 
# 
# 
# 提示：
# 
# 
# 0 
# intervals[i].length == 2
# 0 
# intervals 根据 intervals[i][0] 按 升序 排列
# newInterval.length == 2
# 0 
# 
# 
#

# @lc code=start
def b_find(list, target, fn, is_greater):
    left, right = 0, len(list) - 1
    while left +  1 < right:
        middle = (left + right) // 2
        num_middle = fn(list[middle])

        if target == num_middle:
            return middle
        elif num_middle > target:
            right = middle
        else:
            left = middle

    num_left, num_right = fn(list[left]), fn(list[right])
    if is_greater:
        if num_left > target:
            return left
        elif num_right > target:
            return right
    else:
        if num_right < target:
            return right
        elif num_left < target:
            return left

    return -1


class Solution:
    def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
        if not intervals:
            return [newInterval]

        begin, end = newInterval
        last_left = b_find(intervals, begin, lambda x: x[0], False)
        first_right = b_find(intervals, end, lambda x: x[1], True)

        center_left, center_right = begin, end

        left, right = [], []
        if last_left >= 0:
            left_start, left_end = intervals[last_left]
            if left_end >= begin:
                left = intervals[:last_left]
                center_left = min(left_start, begin)
            else:
                left = intervals[:last_left + 1]

        if first_right >= 0:
            right_begin, right_end = intervals[first_right]
            if right_begin <= end:
                right = intervals[first_right + 1:]
                center_right = max(right_end, end)
            else:
                right = intervals[first_right:]

        return left + [[center_left, center_right]] + right
# @lc code=end
