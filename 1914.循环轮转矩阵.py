#
# @lc app=leetcode.cn id=1914 lang=python3
#
# [1914] 循环轮转矩阵
#
# https://leetcode-cn.com/problems/cyclically-rotating-a-grid/description/
#
# algorithms
# Medium (44.11%)
# Likes:    10
# Dislikes: 0
# Total Accepted:    3.2K
# Total Submissions: 7.3K
# Testcase Example:  '[[40,10],[30,20]]\n1'
#
# 给你一个大小为 m x n 的整数矩阵 grid​​​ ，其中 m 和 n 都是 偶数 ；另给你一个整数 k 。
# 
# 矩阵由若干层组成，如下图所示，每种颜色代表一层：
# 
# 
# 
# 矩阵的循环轮转是通过分别循环轮转矩阵中的每一层完成的。在对某一层进行一次循环旋转操作时，层中的每一个元素将会取代其 逆时针
# 方向的相邻元素。轮转示例如下：
# 
# 返回执行 k 次循环轮转操作后的矩阵。
# 
# 
# 
# 示例 1：
# 
# 输入：grid = [[40,10],[30,20]], k = 1
# 输出：[[10,20],[40,30]]
# 解释：上图展示了矩阵在执行循环轮转操作时每一步的状态。
# 
# 示例 2：
# ⁠ 
# 
# 输入：grid = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]], k = 2
# 输出：[[3,4,8,12],[2,11,10,16],[1,7,6,15],[5,9,13,14]]
# 解释：上图展示了矩阵在执行循环轮转操作时每一步的状态。
# 
# 
# 
# 
# 提示：
# 
# 
# m == grid.length
# n == grid[i].length
# 2 <= m, n <= 50
# m 和 n 都是 偶数
# 1 <= grid[i][j] <=^ 5000
# 1 <= k <= 10^9
# 
# 
#

# @lc code=start
def get_level_length(x1, y1, x2, y2) -> int:
    return 2 * (y2 - y1 + x2 - x1)


def index_to_cord(x1, y1, x2, y2, i) -> tuple[int, int]:
    row, col = x2 - x1 + 1, y2 - y1 + 1

    if i < row:
        return x2 - i, y2
    if i < row + col - 1:
        return x1, y2 - (i - row) - 1
    if i < row + col + row - 2:
        return x1 + i - row - col + 2, y1
    return x2, y1 + i - row - col - row + 3


class Solution:
    def rotateGrid(self, grid: list[list[int]], k: int) -> list[list[int]]:
        result = [[0 for _ in range(len(grid[0]))] for __ in range(len(grid))]
        for level in range(min(len(grid) // 2, len(grid[0]) // 2)):
            x1, x2 = level, len(grid) - level - 1
            y1, y2 = level, len(grid[0]) - level - 1

            level_length = get_level_length(x1, y1, x2, y2)
            real_k = k % level_length

            for i in range(level_length):
                x, y = index_to_cord(x1, y1, x2, y2, i)
                v_x, v_y = index_to_cord(x1, y1, x2, y2, (i - real_k + level_length) % level_length)
                result[x][y] = grid[v_x][v_y]

        return result
# @lc code=end

# print(Solution().rotateGrid([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]], k = 2))
# print(Solution().rotateGrid([[10,1,4,8],[6,6,3,10],[7,4,7,10],[1,10,6,1],[2,1,1,10],[3,8,9,2],[7,1,10,10],[7,1,4,9],[2,2,4,2],[10,7,5,10]], 1))
