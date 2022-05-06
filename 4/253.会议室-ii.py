#
# @lc app=leetcode.cn id=253 lang=python3
#
# [253] 会议室 II
#
# https://leetcode-cn.com/problems/meeting-rooms-ii/description/
#
# algorithms
# Medium (51.23%)
# Likes:    427
# Dislikes: 0
# Total Accepted:    45K
# Total Submissions: 87.8K
# Testcase Example:  '[[0,30],[5,10],[15,20]]'
#
# 给你一个会议时间安排的数组 intervals ，每个会议时间都会包括开始和结束的时间 intervals[i] = [starti, endi] ，返回
# 所需会议室的最小数量 。
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
# 1 <= intervals.length <= 10^4
# 0 <= starti < endi <= 10^6
# 
# 
#


#    0
#  1   2
# 3 4 5 6


# @lc code=start
# from heapq import heapify, heappop


def parent(i: int):
    return (i - 1) // 2


def left(i: int):
    return i * 2 + 1


def right(i: int):
    return left(i) + 1


def swap(l: list, a: int, b: int):
    l[a], l[b] = l[b], l[a]


def shift_up(heap: list, i: int, lt):
    while i > 0:
        p = parent(i)
        if lt(heap[i], heap[p]):
            swap(heap, i, p)
        else:
            break
        i = p


def pick_child(heap: list, i: int, lt):
    l, r = left(i), right(i)

    if l >= len(heap):
        return -1
    if r >= len(heap):
        return l
    if lt(heap[l], heap[r]):
        return l
    return r


def shift_down(heap: list, i: int, lt):
    while i < len(heap):
        child = pick_child(heap, i, lt)
        if child < 0:
            break

        if lt(heap[child], heap[i]):
            swap(heap, i, child)
        else:
            break

        i = child


def heappop(heap: list, lt):
    heap[-1], heap[0] = heap[0], heap[-1]
    result = heap.pop()
    # print('poped::', heap)
    shift_down(heap, 0, lt)
    return result


def heapify(arr: list, lt):
    for i in range(len(arr) - 1, -1, -1):
        shift_down(arr, i, lt)



class Solution:
    def minMeetingRooms(self, intervals: list[list[int]]) -> int:
        def cmp(a, b):
            if a[0] == b[0]:
                return a[1] < b[1]
            return a[0] < b[0]

        t = []
        for begin, end in intervals:
            t.append((begin, 1))
            t.append((end, -1))

        heapify(t, cmp)
        # print(t)

        result = curr = 0
        while t:
            # print(t)
            curr += heappop(t, cmp)[1]
            result = max(result, curr)

        return result
# @lc code=end

s = Solution()
print(s.minMeetingRooms([[6,15],[13,20],[6,17]]))
#           20,-1
#      15,-1       13,1
# 17,-1 

#           15,-1
#      13,1       17,-1
# 20,-1
