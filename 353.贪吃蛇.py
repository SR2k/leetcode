#
# @lc app=leetcode.cn id=353 lang=python3
#
# [353] 贪吃蛇
#
# https://leetcode-cn.com/problems/design-snake-game/description/
#
# algorithms
# Medium (42.67%)
# Likes:    58
# Dislikes: 0
# Total Accepted:    2.2K
# Total Submissions: 5.2K
# Testcase Example:  '["SnakeGame","move","move","move","move","move","move"]\n' +
#  '[[3,2,[[1,2],[0,1]]],["R"],["D"],["R"],["U"],["L"],["U"]]'
#
# 请你设计一个 贪吃蛇游戏，该游戏将会在一个 屏幕尺寸 = 宽度 x 高度 的屏幕上运行。如果你不熟悉这个游戏，可以 点击这里 在线试玩。
# 
# 起初时，蛇在左上角的 (0, 0) 位置，身体长度为 1 个单位。
# 
# 你将会被给出一个数组形式的食物位置序列 food ，其中 food[i] = (ri, ci) 。当蛇吃到食物时，身子的长度会增加 1 个单位，得分也会
# +1 。
# 
# 食物不会同时出现，会按列表的顺序逐一显示在屏幕上。比方讲，第一个食物被蛇吃掉后，第二个食物才会出现。
# 
# 当一个食物在屏幕上出现时，保证 不会 出现在被蛇身体占据的格子里。
# 
# 如果蛇越界（与边界相撞）或者头与 移动后 的身体相撞（即，身长为 4 的蛇无法与自己相撞），游戏结束。
# 
# 实现 SnakeGame 类：
# 
# 
# SnakeGame(int width, int height, int[][] food) 初始化对象，屏幕大小为 height x width
# ，食物位置序列为 food
# int move(String direction) 返回蛇在方向 direction 上移动后的得分。如果游戏结束，返回 -1 。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：
# ["SnakeGame", "move", "move", "move", "move", "move", "move"]
# [[3, 2, [[1, 2], [0, 1]]], ["R"], ["D"], ["R"], ["U"], ["L"], ["U"]]
# 输出：
# [null, 0, 0, 1, 1, 2, -1]
# 
# 解释：
# SnakeGame snakeGame = new SnakeGame(3, 2, [[1, 2], [0, 1]]);
# snakeGame.move("R"); // 返回 0
# snakeGame.move("D"); // 返回 0
# snakeGame.move("R"); // 返回 1 ，蛇吃掉了第一个食物，同时第二个食物出现在 (0, 1)
# snakeGame.move("U"); // 返回 1
# snakeGame.move("L"); // 返回 2 ，蛇吃掉了第二个食物，没有出现更多食物
# snakeGame.move("U"); // 返回 -1 ，蛇与边界相撞，游戏结束
# 
# 
# 
# 
# 提示：
# 
# 
# 1 
# 1 
# food[i].length == 2
# 0 i < height
# 0 i < width
# direction.length == 1
# direction is 'U', 'D', 'L', or 'R'.
# 最多调用 10^4 次 move 方法
# 
# 
#

# @lc code=start
from collections import deque


DIRECTIONS = {
    'U': (-1, 0),
    'D': (1, 0),
    'L': (0, -1),
    'R': (0, 1),
}


class SnakeGame:
    def __init__(self, width: int, height: int, food: list[list[int]]):
        self.food = deque()
        for i, j in food:
            self.food.append((i, j))

        self.width = width
        self.height = height

        self.body_set = {(0, 0),}
        self.body = deque([(0, 0)])


    def move(self, direction: str) -> int:
        di, dj = DIRECTIONS[direction]
        i, j = self.body[0]
        next_head = (i + di, j + dj)

        if not (0 <= next_head[1] < self.width and 0 <= next_head[0] < self.height):
            return -1

        food = self.food[0] if self.food else None
        if next_head == food:
            self.food.popleft()
        else:
            self.body_set.remove(self.body.pop())

        if next_head in self.body_set:
            return -1

        self.body.appendleft(next_head)
        self.body_set.add(next_head)
        return len(self.body_set) - 1

# Your SnakeGame object will be instantiated and called as such:
# obj = SnakeGame(width, height, food)
# param_1 = obj.move(direction)
# @lc code=end

sn = None
# cmd = ["SnakeGame", "move", "move", "move", "move", "move", "move"]
# q = [[3, 2, [[1, 2], [0, 1]]], ["R"], ["D"], ["R"], ["U"], ["L"], ["U"]]

# cmd = ["SnakeGame","move","move"]
# q = [[1,2,[[1,0]]],["D"],["D"]]

cmd = ["SnakeGame","move","move","move","move","move","move","move","move","move","move","move","move"]
q = [[3,3,[[2,0],[0,0],[0,2],[2,2]]],["D"],["D"],["R"],["U"],["U"],["L"],["D"],["R"],["R"],["U"],["L"],["D"]]


for i, c in enumerate(cmd):
    if c == 'SnakeGame':
        sn = SnakeGame(q[i][0], q[i][1], q[i][2])
    elif c == 'move':
        print(sn.move(q[i][0]))

