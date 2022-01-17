#
# @lc app=leetcode.cn id=397 lang=python3
#
# [397] 整数替换
#
# https://leetcode-cn.com/problems/integer-replacement/description/
#
# algorithms
# Medium (37.76%)
# Likes:    98
# Dislikes: 0
# Total Accepted:    14.9K
# Total Submissions: 39.4K
# Testcase Example:  '8'
#
# 给定一个正整数 n ，你可以做如下操作：
# 
# 
# 如果 n 是偶数，则用 n / 2替换 n 。
# 如果 n 是奇数，则可以用 n + 1或n - 1替换 n 。
# 
# 
# n 变为 1 所需的最小替换次数是多少？
# 
# 
# 
# 示例 1：
# 
# 
# 输入：n = 8
# 输出：3
# 解释：8 -> 4 -> 2 -> 1
# 
# 
# 示例 2：
# 
# 
# 输入：n = 7
# 输出：4
# 解释：7 -> 8 -> 4 -> 2 -> 1
# 或 7 -> 6 -> 3 -> 2 -> 1
# 
# 
# 示例 3：
# 
# 
# 输入：n = 4
# 输出：2
# 
# 
# 
# 
# 提示：
# 
# 
# 1 
# 
# 
#

# @lc code=start
from collections import deque


class Solution:
    def integerReplacement(self, n: int) -> int:
        if n == 1:
            return 0


        visited = { n }
        queue = deque(visited)
        level_count = 0

        while True:
            level_length = len(queue)
            level_count += 1

            for _ in range(level_length):
                curr = queue.popleft()

                if curr % 2 == 0:
                    next_nums = [curr // 2]
                else:
                    next_nums = [curr - 1, curr + 1]

                for n in next_nums:
                    if n == 1:
                        return level_count

                    if not n in visited:
                        visited.add(n)
                        queue.append(n)
# @lc code=end
