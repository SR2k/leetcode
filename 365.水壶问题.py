#
# @lc app=leetcode.cn id=365 lang=python3
#
# [365] 水壶问题
#
# https://leetcode-cn.com/problems/water-and-jug-problem/description/
#
# algorithms
# Medium (35.83%)
# Likes:    299
# Dislikes: 0
# Total Accepted:    31.2K
# Total Submissions: 86.9K
# Testcase Example:  '3\n5\n4'
#
# 有两个容量分别为 x升 和 y升 的水壶以及无限多的水。请判断能否通过使用这两个水壶，从而可以得到恰好 z升 的水？
# 
# 如果可以，最后请用以上水壶中的一或两个来盛放取得的 z升 水。
# 
# 你允许：
# 
# 
# 装满任意一个水壶
# 清空任意一个水壶
# 从一个水壶向另外一个水壶倒水，直到装满或者倒空
# 
# 
# 示例 1: (From the famous "Die Hard" example)
# 
# 输入: x = 3, y = 5, z = 4
# 输出: True
# 
# 
# 示例 2:
# 
# 输入: x = 2, y = 6, z = 5
# 输出: False
# 
# 
#

# @lc code=start
from collections import deque


def get_next(jugs: tuple[int, int], jug_0_capacity: int, jug_1_capacity: int) -> set[tuple[int, int]]:
    ret = {jugs}
    ret.add((0, jugs[1]))
    ret.add((jugs[0], 0))
    ret.add((jug_0_capacity, jugs[1]))
    ret.add((jugs[0], jug_1_capacity))

    j0_left, j1_left = jug_0_capacity - jugs[0], jug_1_capacity - jugs[1]

    if jugs[1]:
        p0 = (jug_0_capacity, jugs[1] - j0_left) if jugs[1] >= j0_left else (jugs[0] + jugs[1], 0)
        ret.add(p0)
    if jugs[0]:
        p1 = (jugs[0] - j0_left, jug_1_capacity) if jugs[0] >= j1_left else (0, jugs[0] + jugs[1])
        ret.add(p1)

    ret.remove(jugs)

    return ret

class Solution:
    def canMeasureWater(self, jug1Capacity: int, jug2Capacity: int, targetCapacity: int) -> bool:
        begin = (0, 0)
        queue = deque([begin])
        visited = {begin}

        while queue:
            curr = queue.popleft()
            next = get_next(curr, jug1Capacity, jug2Capacity)

            for n in next:
                if n[0] + n[1] == targetCapacity:
                    return True
                if n not in visited:
                    visited.add(n)
                    queue.append(n)

        return False
# @lc code=end
