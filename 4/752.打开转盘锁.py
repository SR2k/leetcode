#
# @lc app=leetcode.cn id=752 lang=python3
#
# [752] 打开转盘锁
#
# https://leetcode-cn.com/problems/open-the-lock/description/
#
# algorithms
# Medium (52.93%)
# Likes:    472
# Dislikes: 0
# Total Accepted:    86.9K
# Total Submissions: 164.1K
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
from heapq import heappop, heappush


class AStarNode:
    def __init__(self, val: str, passed: int, target: str) -> None:
        self.val = val
        self.passed = passed
        self.cost = passed + AStarNode.get_pending(val, target)

        # print(val, target, 'yy', passed, 'xx', self.cost)


    def __lt__(self, other: 'AStarNode'):
        return self.cost <= other.cost


    def next_moves(self) -> list[int]:
        result = []

        for i in range(len(self.val)):
            temp = list(self.val)
            temp[i] = str((int(temp[i]) + 1) % 10)
            result.append("".join(temp))

            temp = list(self.val)
            temp[i] = str((int(temp[i]) - 1 + 10) % 10)
            result.append("".join(temp))

        return result


    @staticmethod
    def get_pending(curr: list[int], target: str):
        result = 0
        for i in range(len(curr)):
            move = (ord(curr[i]) - ord(target[i]) + 10) % 10
            move = min(move, 10 - move)
            result += move
        return result


ENTRY = '0000'


class Solution:
    def openLock(self, deadends: list[str], target: str) -> int:
        queue = [AStarNode(ENTRY, 0, target)]
        seen = set([ENTRY])
        deadends = set(deadends)

        if target in deadends or ENTRY in deadends:
            return -1

        while queue:
            move = heappop(queue)

            if move.val == target:
                return move.passed

            for n in move.next_moves():
                if n not in deadends and n not in seen:
                    heappush(queue, AStarNode(n, move.passed + 1, target))
                    seen.add(n)

        return -1
# @lc code=end

# print(AStarNode('0000', 0, '0000').next_moves())

s = Solution()
print(s.openLock(["0201","0101","0102","1212","2002"], "0202"))
