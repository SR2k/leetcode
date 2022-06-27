#
# @lc app=leetcode.cn id=362 lang=python3
#
# [362] 敲击计数器
#
# https://leetcode.cn/problems/design-hit-counter/description/
#
# algorithms
# Medium (69.05%)
# Likes:    82
# Dislikes: 0
# Total Accepted:    5.1K
# Total Submissions: 7.4K
# Testcase Example:  '["HitCounter","hit","hit","hit","getHits","hit","getHits","getHits"]\n' +
#  '[[],[1],[2],[3],[4],[300],[300],[301]]'
#
# 设计一个敲击计数器，使它可以统计在过去 5 分钟内被敲击次数。（即过去 300 秒）
# 
# 您的系统应该接受一个时间戳参数 timestamp (单位为 秒 )，并且您可以假定对系统的调用是按时间顺序进行的(即 timestamp
# 是单调递增的)。几次撞击可能同时发生。
# 
# 实现 HitCounter 类:
# 
# 
# HitCounter() 初始化命中计数器系统。
# void hit(int timestamp) 记录在 timestamp ( 单位为秒 )发生的一次命中。在同一个 timestamp
# 中可能会出现几个点击。
# int getHits(int timestamp) 返回 timestamp 在过去 5 分钟内(即过去 300 秒)的命中次数。
# 
# 
# 
# 
# 示例 1:
# 
# 
# 输入：
# ["HitCounter", "hit", "hit", "hit", "getHits", "hit", "getHits", "getHits"]
# [[], [1], [2], [3], [4], [300], [300], [301]]
# 输出：
# [null, null, null, null, 3, null, 4, 3]
# 
# 解释：
# HitCounter counter = new HitCounter();
# counter.hit(1);// 在时刻 1 敲击一次。
# counter.hit(2);// 在时刻 2 敲击一次。
# counter.hit(3);// 在时刻 3 敲击一次。
# counter.getHits(4);// 在时刻 4 统计过去 5 分钟内的敲击次数, 函数返回 3 。
# counter.hit(300);// 在时刻 300 敲击一次。
# counter.getHits(300); // 在时刻 300 统计过去 5 分钟内的敲击次数，函数返回 4 。
# counter.getHits(301); // 在时刻 301 统计过去 5 分钟内的敲击次数，函数返回 3 。
# 
# 
# 
# 
# 提示:
# 
# 
# 1 <= timestamp <= 2 * 10^9
# 所有对系统的调用都是按时间顺序进行的（即 timestamp 是单调递增的）
# hit and getHits 最多被调用 300 次
# 
# 
# 
# 
# 进阶: 如果每秒的敲击次数是一个很大的数字，你的计数器可以应对吗？
# 
#

# @lc code=start
FLAG_FIRST_GTE, FLAG_LAST_LTE = 0, 1


class HitCounter:
    def __init__(self):
        self.hits = []
        self.interval = 300

    def hit(self, timestamp: int) -> None:
        self.hits.append(timestamp)


    def getHits(self, timestamp: int) -> int:
        begin = HitCounter.b_find(self.hits, timestamp - self.interval + 1, FLAG_FIRST_GTE)
        end = HitCounter.b_find(self.hits, timestamp, FLAG_LAST_LTE)

        return max(end - begin + 1, 0)


    @staticmethod
    def b_find(arr: list[int], target: int, flag: int):
        if not arr:
            return 0 if flag == FLAG_FIRST_GTE else -1

        left, right = 0, len(arr) - 1
        while left + 1 < right:
            middle = (left + right) // 2

            if arr[middle] > target:
                right = middle
            elif arr[middle] < target:
                left = middle
            elif flag == FLAG_FIRST_GTE:
                right = middle
            else:
                left = middle

        if flag == FLAG_FIRST_GTE:
            if arr[left] >= target:
                return left
            if arr[right] >= target:
                return right
            return len(arr)

        if arr[right] <= target:
            return right
        if arr[left] <= target:
            return left
        return -1
# @lc code=end


# ["HitCounter","getHits","getHits","getHits","hit","hit","getHits"]
# [[],[100],[200],[300],[300],[401],[402]]
