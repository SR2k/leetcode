#
# @lc app=leetcode.cn id=752 lang=python3
#
# [752] 打开转盘锁
#
# https://leetcode-cn.com/problems/open-the-lock/description/
#
# algorithms
# Medium (53.10%)
# Likes:    457
# Dislikes: 0
# Total Accepted:    83.2K
# Total Submissions: 157K
# Testcase Example:  '["0201","0101","0102","1212","2002"]\n"0202"'
#
# 你有一个带有四个圆形拨轮的转盘锁。每个拨轮都有10个数字： '0', '1', '2', '3', '4', '5', '6', '7', '8',
# '9' 。每个拨轮可以自由旋转：例如把 '9' 变为 '0'，'0' 变为 '9' 。每次旋转都只能旋转一个拨轮的一位数字。
# 
# 锁的初始数字为 '0000' ，一个代表四个拨轮的数字的字符串。
# 
# 列表 deadends 包含了一组死亡数字，一旦拨轮的数字和列表里的任何一个元素相同，这个锁将会被永久锁定，无法再被旋转。
# 
# 字符串 target 代表可以解锁的数字，你需要给出解锁需要的最小旋转次数，如果无论如何不能解锁，返回 -1 。
# 
# 
# 
# 示例 1:
# 
# 
# 输入：deadends = ["0201","0101","0102","1212","2002"], target = "0202"
# 输出：6
# 解释：
# 可能的移动序列为 "0000" -> "1000" -> "1100" -> "1200" -> "1201" -> "1202" -> "0202"。
# 注意 "0000" -> "0001" -> "0002" -> "0102" -> "0202" 这样的序列是不能解锁的，
# 因为当拨动到 "0102" 时这个锁就会被锁定。
# 
# 
# 示例 2:
# 
# 
# 输入: deadends = ["8888"], target = "0009"
# 输出：1
# 解释：把最后一位反向旋转一次即可 "0000" -> "0009"。
# 
# 
# 示例 3:
# 
# 
# 输入: deadends = ["8887","8889","8878","8898","8788","8988","7888","9888"],
# target = "8888"
# 输出：-1
# 解释：无法旋转到目标数字且不被锁定。
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= deadends.length <= 500
# deadends[i].length == 4
# target.length == 4
# target 不在 deadends 之中
# target 和 deadends[i] 仅由若干位数字组成
# 
# 
#

# @lc code=start
from heapq import heappush, heappop


class Node(object):
    @staticmethod
    def get_h(a, target: str):
        res = 0
        for i, c in enumerate(a):
            diff = abs(int(c) - int(target[i]))
            res += min(diff, 10 - diff)
        return res


    def __init__(self, value: str, g: int, target: str) -> None:
        self.value = value
        self.g = g
        self.f = g + Node.get_h(value, target)


    def __lt__(self, other: 'Node'):
        return self.f < other.f


class Solution:
    def openLock(self, deadends: list[str], target: str) -> int:
        dead = set(deadends)
        if '0000' in dead or target in dead:
            return -1
        if target == '0000':
            return 0

        pq = [Node('0000', 0, target)]
        seen = set(pq)

        while pq:
            curr = heappop(pq)

            for next in Solution.get_next(curr.value):
                if next in seen or next in dead:
                    continue
                if next == target:
                    return curr.g + 1

                heappush(pq, Node(next, curr.g + 1, target))
                seen.add(next)

        return -1


    @staticmethod
    def prev(digit: str):
        return str(int(digit) - 1) if digit != '0' else '9'

    @staticmethod
    def next(digit: str):
        return str(int(digit) + 1) if digit != '9' else '0'


    @staticmethod
    def get_next(curr: str):
        for i, d in enumerate(curr):
            prev = Solution.prev(d)
            yield curr[:i] + prev + curr[i + 1:]
            next = Solution.next(d)
            yield curr[:i] + next + curr[i + 1:]
# @lc code=end
