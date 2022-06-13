#
# @lc app=leetcode.cn id=54 lang=python3
#
# [54] 螺旋矩阵
#
# https://leetcode.cn/problems/spiral-matrix/description/
#
# algorithms
# Medium (48.81%)
# Likes:    1118
# Dislikes: 0
# Total Accepted:    269.7K
# Total Submissions: 552.5K
# Testcase Example:  '[[1,2,3],[4,5,6],[7,8,9]]'
#
# 给你一个 m 行 n 列的矩阵 matrix ，请按照 顺时针螺旋顺序 ，返回矩阵中的所有元素。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：matrix = [[1,2,3],[4,5,6],[7,8,9]]
# 输出：[1,2,3,6,9,8,7,4,5]
# 
# 
# 示例 2：
# 
# 
# 输入：matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
# 输出：[1,2,3,4,8,12,11,10,9,5,6,7]
# 
# 
# 
# 
# 提示：
# 
# 
# m == matrix.length
# n == matrix[i].length
# 1 
# -100 
# 
# 
#

# @lc code=start
DIRECTIONS = (0, 1), (1, 0), (0, -1), (-1, 0)
MASK = (0, 1), (1, 0), (0, 1), (1, 0)
EDGE_MOVE = 1, -1, -1, 1


class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        m, n = len(matrix), len(matrix[0])
        edges = [0, n - 1, m - 1, 0]
        d = 0
        i, j = 0, 0
        result = []

        while len(result) < m * n:
            result.append(matrix[i][j])

            mask_i, mask_j = MASK[d]
            side = mask_i * i + mask_j * j

            next_direction = (d + 1) % 4
            if side == edges[next_direction]:
                edges[d] += EDGE_MOVE[d]
                d = next_direction

            di, dj = DIRECTIONS[d]
            i += di
            j += dj

        return result
# @lc code=end
