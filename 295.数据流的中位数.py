#
# @lc app=leetcode.cn id=295 lang=python3
#
# [295] 数据流的中位数
#
# https://leetcode-cn.com/problems/find-median-from-data-stream/description/
#
# algorithms
# Hard (52.53%)
# Likes:    665
# Dislikes: 0
# Total Accepted:    79.3K
# Total Submissions: 151K
# Testcase Example:  '["MedianFinder","addNum","addNum","findMedian","addNum","findMedian"]\n' +
#  '[[],[1],[2],[],[3],[]]'
#
# 中位数是有序列表中间的数。如果列表长度是偶数，中位数则是中间两个数的平均值。
# 
# 例如，
# 
# [2,3,4] 的中位数是 3
# 
# [2,3] 的中位数是 (2 + 3) / 2 = 2.5
# 
# 设计一个支持以下两种操作的数据结构：
# 
# 
# void addNum(int num) - 从数据流中添加一个整数到数据结构中。
# double findMedian() - 返回目前所有元素的中位数。
# 
# 
# 示例：
# 
# addNum(1)
# addNum(2)
# findMedian() -> 1.5
# addNum(3) 
# findMedian() -> 2
# 
# 进阶:
# 
# 
# 如果数据流中所有整数都在 0 到 100 范围内，你将如何优化你的算法？
# 如果数据流中 99% 的整数都在 0 到 100 范围内，你将如何优化你的算法？
# 
# 
#


#      0
#    1   2
#   3 4 5 6


# @lc code=start
def parent_index(i: int):
    return (i - 1) // 2


def left_index(i: int):
    return i * 2 + 1


def right_index(i: int):
    return left_index(i) + 1


def pick_child(arr: list, i: int):
    l, r = left_index(i), right_index(i)

    if l >= len(arr):
        return None
    if r >= len(arr):
        return l

    if arr[l][0] <= arr[r][0]:
        return l
    return r


def swap(arr: list, i: int, j: int):
    arr[i], arr[j] = arr[j], arr[i]


def shift_up(arr: list[tuple[int, int]], i: int):
    while i > 0:
        p = parent_index(i)
        if arr[p][0] <= arr[i][0]:
            break
        swap(arr, p, i)
        i = p


def shift_down(arr: list[tuple[int, int]], i: int):
    while i < len(arr):
        c = pick_child(arr, i)
        if c is None or arr[i][0] <= arr[c][0]:
            break
        swap(arr, c, i)
        i = c


def heappush(arr: list[tuple[int, int]], item: tuple[int, int]):
    arr.append(item)
    shift_up(arr, len(arr) - 1)


def heappop(arr: list[tuple[int, int]]):
    swap(arr, 0, len(arr) - 1)
    result = arr.pop()
    shift_down(arr, 0)
    return result

class MedianFinder:
    def __init__(self):
        # 大根堆，小数
        self.heap1 = []
        # 小根堆，大数
        self.heap2 = []


    def addNum(self, num: int) -> None:
        if not self.heap1 or num >= self.heap1[0][1]:
            heappush(self.heap2, (num, num))
        else:
            heappush(self.heap1, (-num, num))

        while len(self.heap1) < len(self.heap2):
            _, num = heappop(self.heap2)
            heappush(self.heap1, (-num, num))
        while len(self.heap1) > len(self.heap2) + 1:
            _, num = heappop(self.heap1)
            heappush(self.heap2, (num, num))

        # print([x[1] for x in self.heap1], [x[1] for x in self.heap2])


    def findMedian(self) -> float:
        if len(self.heap1) == len(self.heap2):
            return (self.heap1[0][1] + self.heap2[0][1]) / 2
        return self.heap1[0][1]
# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
# @lc code=end

# ["MedianFinder","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian"]
# [[],[6],[],[10],[],[2],[],[6],[],[5],[],[0],[],[6],[],[3],[],[1],[],[0],[],[0],[]]

# 6, 10, 2, 6, 5, 0, 6, 3, 1, 0, 0


# [null,null,6.00000,null,8.00000,null,6.00000,null,6.00000,null,6.00000,null,5.50000,null,6.00000,null,5.50000,null,5.00000,null,3.50000,null,2.00000]

# [null,null,6.00000,null,8.00000,null,6.00000,null,6.00000,null,6.00000,null,5.50000,null,6.00000,null,5.50000,null,5.00000,null,4.00000,null,3.00000]

#     2
#   3   0
#  0 1

x = [(-i, i) for i in [6, 5, 0, 2, 3]]
heappop(x)
print([i[1] for i in x])


#        5
#     2    0
#   3  1 0

#      5
#    3  0
#   2
