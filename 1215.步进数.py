#
# @lc app=leetcode.cn id=1215 lang=python3
#
# [1215] 步进数
#
# https://leetcode-cn.com/problems/stepping-numbers/description/
#
# algorithms
# Medium (40.53%)
# Likes:    21
# Dislikes: 0
# Total Accepted:    1.8K
# Total Submissions: 4.3K
# Testcase Example:  '0\n21'
#
# 如果一个整数上的每一位数字与其相邻位上的数字的绝对差都是 1，那么这个数就是一个「步进数」。
# 
# 例如，321 是一个步进数，而 421 不是。
# 
# 给你两个整数，low 和 high，请你找出在 [low, high] 范围内的所有步进数，并返回 排序后 的结果。
# 
# 
# 
# 示例：
# 
# 输入：low = 0, high = 21
# 输出：[0,1,2,3,4,5,6,7,8,9,10,12,21]
# 
# 
# 
# 
# 提示：
# 
# 
# 0 <= low <= high <= 2 * 10^9
# 
# 
#

# @lc code=start
from collections import deque


class Solution:
    def countSteppingNumbers(self, low: int, high: int) -> list[int]:
        queue: deque[int] = deque(range(10))
        ret: list[int] = []

        while True:
            curr_len = len(queue)
            for _ in range(curr_len):
                curr_num = queue.popleft()
                if low <= curr_num <= high:
                    ret.append(curr_num)
                elif curr_num > high:
                    return ret

                if curr_num == 0: continue
                last_digit = curr_num % 10

                if last_digit == 0:
                    queue.append(curr_num * 10 + last_digit + 1)
                elif last_digit == 9:
                    queue.append(curr_num * 10 + last_digit - 1)
                else:
                    queue.append(curr_num * 10 + last_digit - 1)
                    queue.append(curr_num * 10 + last_digit + 1)
# @lc code=end

