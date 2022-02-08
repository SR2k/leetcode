#
# @lc app=leetcode.cn id=635 lang=python3
#
# [635] 设计日志存储系统
#
# https://leetcode-cn.com/problems/design-log-storage-system/description/
#
# algorithms
# Medium (55.50%)
# Likes:    41
# Dislikes: 0
# Total Accepted:    3.6K
# Total Submissions: 6.5K
# Testcase Example:  '["LogSystem","put","put","put","retrieve","retrieve"]\n' +
#  '[[],[1,"2017:01:01:23:59:59"],[2,"2017:01:01:22:59:59"],[3,"2016:01:01:00:00:00"],["2016:01:01:01:01:01","2017:01:01:23:00:00","Year"],["2016:01:01:01:01:01","2017:01:01:23:00:00","Hour"]]'
#
# 你将获得多条日志，每条日志都有唯一的 id 和 timestamp ，timestamp 是形如
# Year:Month:Day:Hour:Minute:Second 的字符串，2017:01:01:23:59:59 ，所有值域都是零填充的十进制数。
# 
# 实现 LogSystem 类：
# 
# 
# LogSystem() 初始化 LogSystem 对象
# void put(int id, string timestamp) 给定日志的 id 和 timestamp ，将这个日志存入你的存储系统中。
# int[] retrieve(string start, string end, string granularity) 返回在给定时间区间
# [start, end] （包含两端）内的所有日志的 id 。start 、end 和 timestamp 的格式相同，granularity
# 表示考虑的时间粒度（例如，精确到 Day、Minute 等）。例如 start = "2017:01:01:23:59:59"、end =
# "2017:01:02:23:59:59" 且 granularity = "Day" 意味着需要查找从 Jan. 1st 2017 到 Jan. 2nd
# 2017 范围内的日志，可以忽略日志的 Hour、Minute 和 Second 。
# 
# 
# 
# 示例：
# 
# 
# 输入：
# ["LogSystem", "put", "put", "put", "retrieve", "retrieve"]
# [[], [1, "2017:01:01:23:59:59"], [2, "2017:01:01:22:59:59"], [3,
# "2016:01:01:00:00:00"], ["2016:01:01:01:01:01", "2017:01:01:23:00:00",
# "Year"], ["2016:01:01:01:01:01", "2017:01:01:23:00:00", "Hour"]]
# 输出：
# [null, null, null, null, [3, 2, 1], [2, 1]]
# 
# 解释：
# LogSystem logSystem = new LogSystem();
# logSystem.put(1, "2017:01:01:23:59:59");
# logSystem.put(2, "2017:01:01:22:59:59");
# logSystem.put(3, "2016:01:01:00:00:00");
# 
# // 返回 [3,2,1]，返回从 2016 年到 2017 年所有的日志。
# logSystem.retrieve("2016:01:01:01:01:01", "2017:01:01:23:00:00", "Year");
# 
# // 返回 [2,1]，返回从 Jan. 1, 2016 01:XX:XX 到 Jan. 1, 2017 23:XX:XX 之间的所有日志
# // 不返回日志 3 因为记录时间 Jan. 1, 2016 00:00:00 超过范围的起始时间
# logSystem.retrieve("2016:01:01:01:01:01", "2017:01:01:23:00:00",
# "Hour");
# 
# 
# 
# 
# 提示：
# 
# 
# 1 
# 2000 
# 1 
# 1 
# 0 
# 0 
# granularity 是这些值 ["Year", "Month", "Day", "Hour", "Minute", "Second"] 之一
# 最多调用 500 次 put 和 retrieve
# 
# 
#

# @lc code=start
from sortedcontainers import SortedList


GRANULARITY_MAP = {
    'Year': 4,
    'Month': 7,
    'Day': 10,
    'Hour': 13,
    'Minute': 16,
    'Second': 19,
}


class LogSystem:
    def __init__(self):
        self.ss = SortedList(key=lambda x: x[1])


    def put(self, id: int, timestamp: str) -> None:
        self.ss.add((id, timestamp))


    def b_find(self, target: str, granularity: str, is_start: bool) -> int:
        if not self.ss:
            return -1

        left, right = 0, len(self.ss) - 1
        slice_end = GRANULARITY_MAP[granularity]
        target = target[:slice_end]

        while left + 1 < right:
            middle = (left + right) // 2
            middle_ts = self.ss[middle][1][:slice_end]

            if is_start:
                if middle_ts >= target:
                    right = middle
                else:
                    left = middle

            else:
                if middle_ts <= target:
                    left = middle
                elif middle_ts > target:
                    right = middle

        if is_start:
            left_ts = self.ss[left][1][:slice_end]
            if left_ts >= target:
                return left
            right_ts = self.ss[right][1][:slice_end]
            if right_ts >= target:
                return right
            return -1
        else:
            right_ts = self.ss[right][1][:slice_end]
            if right_ts <= target:
                return right
            left_ts = self.ss[left][1][:slice_end]
            if left_ts <= target:
                return left
            return -1


    def retrieve(self, start: str, end: str, granularity: str) -> list[int]:
        l, r = self.b_find(start, granularity, True), self.b_find(end, granularity, False)
        if l < 0 or r < 0:
            return []
        return [x [0] for x in self.ss[l:r + 1]]

# Your LogSystem object will be instantiated and called as such:
# obj = LogSystem()
# obj.put(id,timestamp)
# param_2 = obj.retrieve(start,end,granularity)
# @lc code=end

