#
# @lc app=leetcode.cn id=352 lang=python3
#
# [352] 将数据流变为多个不相交区间
#
# https://leetcode-cn.com/problems/data-stream-as-disjoint-intervals/description/
#
# algorithms
# Hard (59.29%)
# Likes:    83
# Dislikes: 0
# Total Accepted:    6.3K
# Total Submissions: 9.9K
# Testcase Example:  '["SummaryRanges","addNum","getIntervals","addNum","getIntervals","addNum","getIntervals","addNum","getIntervals","addNum","getIntervals"]\n' +
#  '[[],[1],[],[3],[],[7],[],[2],[],[6],[]]'
#
#  给你一个由非负整数 a1, a2, ..., an 组成的数据流输入，请你将到目前为止看到的数字总结为不相交的区间列表。
# 
# 实现 SummaryRanges 类：
# 
# 
# 
# 
# SummaryRanges() 使用一个空数据流初始化对象。
# void addNum(int val) 向数据流中加入整数 val 。
# int[][] getIntervals() 以不相交区间 [starti, endi] 的列表形式返回对数据流中整数的总结。
# 
# 
# 
# 
# 示例：
# 
# 
# 输入：
# ["SummaryRanges", "addNum", "getIntervals", "addNum", "getIntervals",
# "addNum", "getIntervals", "addNum", "getIntervals", "addNum", "getIntervals"]
# [[], [1], [], [3], [], [7], [], [2], [], [6], []]
# 输出：
# [null, null, [[1, 1]], null, [[1, 1], [3, 3]], null, [[1, 1], [3, 3], [7,
# 7]], null, [[1, 3], [7, 7]], null, [[1, 3], [6, 7]]]
# 
# 解释：
# SummaryRanges summaryRanges = new SummaryRanges();
# summaryRanges.addNum(1);      // arr = [1]
# summaryRanges.getIntervals(); // 返回 [[1, 1]]
# summaryRanges.addNum(3);      // arr = [1, 3]
# summaryRanges.getIntervals(); // 返回 [[1, 1], [3, 3]]
# summaryRanges.addNum(7);      // arr = [1, 3, 7]
# summaryRanges.getIntervals(); // 返回 [[1, 1], [3, 3], [7, 7]]
# summaryRanges.addNum(2);      // arr = [1, 2, 3, 7]
# summaryRanges.getIntervals(); // 返回 [[1, 3], [7, 7]]
# summaryRanges.addNum(6);      // arr = [1, 2, 3, 6, 7]
# summaryRanges.getIntervals(); // 返回 [[1, 3], [6, 7]]
# 
# 
# 
# 
# 提示：
# 
# 
# 0 <= val <= 10^4
# 最多调用 addNum 和 getIntervals 方法 3 * 10^4 次
# 
# 
# 
# 
# 
# 
# 进阶：如果存在大量合并，并且与数据流的大小相比，不相交区间的数量很小，该怎么办?
# 
#

# @lc code=start
from sortedcontainers import SortedList


class SummaryRanges:
    def __init__(self):
        self.list = SortedList(key=lambda x: x[0])


    def b_find(self, val: int, right_flag = False) -> tuple[int, int]:
        if not self.list:
            return -1

        left, right = 0, len(self.list) - 1

        while left + 1 < right:
            middle = (left + right) // 2
            middle_val = self.list[middle][0]

            if middle_val == val:
                return middle
            elif middle_val > val:
                right = middle
            else:
                left = middle

        if right_flag:
            if self.list[left][0] >= val:
                return left
            if self.list[right][0] >= val:
                return right
        else:
            if self.list[right][0] <= val:
                return right
            if self.list[left][0] <= val:
                return left

        return -1


    def addNum(self, val: int) -> None:
        l, r = self.b_find(val), self.b_find(val, True)
        l_merge = l >= 0 and self.list[l][1] == val - 1
        r_merge = r >= 0 and self.list[r][0] == val + 1

        if l >= 0 and self.list[l][0] <= val <= self.list[l][1]:
            pass

        elif r >= 0 and self.list[r][0] <= val <= self.list[r][1]:
            pass

        elif l_merge and r_merge:
            a, _ = self.list[l]
            _, b = self.list[r]
            del self.list[r]
            del self.list[l]
            self.list.add((a, b))

        elif l_merge:
            a, _ = self.list[l]
            del self.list[l]
            self.list.add((a, val))

        elif r_merge:
            _, b = self.list[r]
            del self.list[r]
            self.list.add((val, b))

        else:
            self.list.add((val, val))


    def getIntervals(self) -> list[list[int]]:
        return [list(x) for x in self.list]

# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(val)
# param_2 = obj.getIntervals()
# @lc code=end

sr = None
cmd = ["SummaryRanges", "addNum", "getIntervals", "addNum", "getIntervals", "addNum", "getIntervals", "addNum", "getIntervals", "addNum", "getIntervals"]
q = [[], [1], [], [3], [], [7], [], [2], [], [6], []]

for i, c in enumerate(cmd):
    if c == 'SummaryRanges':
        sr = SummaryRanges()
    elif c == 'addNum':
        sr.addNum(q[i][0])
        print('>>> added', q[i][0])
    elif c == 'getIntervals':
        print(sr.getIntervals())
