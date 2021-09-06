#
# @lc app=leetcode.cn id=949 lang=python3
#
# [949] 给定数字能组成的最大时间
#
# https://leetcode-cn.com/problems/largest-time-for-given-digits/description/
#
# algorithms
# Medium (36.92%)
# Likes:    69
# Dislikes: 0
# Total Accepted:    7.8K
# Total Submissions: 21.3K
# Testcase Example:  '[1,2,3,4]'
#
# 给定一个由 4 位数字组成的数组，返回可以设置的符合 24 小时制的最大时间。
# 
# 24 小时格式为 "HH:MM" ，其中 HH 在 00 到 23 之间，MM 在 00 到 59 之间。最小的 24 小时制时间是 00:00
# ，而最大的是 23:59 。从 00:00 （午夜）开始算起，过得越久，时间越大。
# 
# 以长度为 5 的字符串，按 "HH:MM" 格式返回答案。如果不能确定有效时间，则返回空字符串。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：arr = [1,2,3,4]
# 输出："23:41"
# 解释：有效的 24 小时制时间是
# "12:34"，"12:43"，"13:24"，"13:42"，"14:23"，"14:32"，"21:34"，"21:43"，"23:14" 和
# "23:41" 。这些时间中，"23:41" 是最大时间。
# 
# 
# 示例 2：
# 
# 
# 输入：arr = [5,5,5,5]
# 输出：""
# 解释：不存在有效的 24 小时制时间，因为 "55:55" 无效。
# 
# 
# 示例 3：
# 
# 
# 输入：arr = [0,0,0,0]
# 输出："00:00"
# 
# 
# 示例 4：
# 
# 
# 输入：arr = [0,0,1,0]
# 输出："10:00"
# 
# 
# 
# 
# 提示：
# 
# 
# arr.length == 4
# 0 
# 
# 
#

# @lc code=start
from itertools import permutations


def check(arr: tuple[int, int, int, int]) -> bool:
    h = arr[0] * 10 + arr[1]
    m = arr[2] * 10 + arr[3]

    return 0 <= h <= 23 and 0 <= m <= 59


class Solution:
    def largestTimeFromDigits(self, arr: list[int]) -> str:
        arr.sort(key=lambda x: -x)
        for p in permutations(arr):
            if check(p):
                return f"{p[0]}{p[1]}:{p[2]}{p[3]}"

        return ""

# @lc code=end

