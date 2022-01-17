#
# @lc app=leetcode.cn id=1594 lang=python3
#
# [1594] 矩阵的最大非负积
#
# https://leetcode-cn.com/problems/maximum-non-negative-product-in-a-matrix/description/
#
# algorithms
# Medium (31.36%)
# Likes:    31
# Dislikes: 0
# Total Accepted:    4.3K
# Total Submissions: 13.8K
# Testcase Example:  '[[-1,-2,-3],[-2,-3,-3],[-3,-3,-2]]'
#
# 给你一个大小为 rows x cols 的矩阵 grid 。最初，你位于左上角 (0, 0) ，每一步，你可以在矩阵中 向右 或 向下 移动。
# 
# 在从左上角 (0, 0) 开始到右下角 (rows - 1, cols - 1) 结束的所有路径中，找出具有 最大非负积
# 的路径。路径的积是沿路径访问的单元格中所有整数的乘积。
# 
# 返回 最大非负积 对 10^9 + 7 取余 的结果。如果最大积为负数，则返回 -1 。
# 
# 注意，取余是在得到最大积之后执行的。
# 
# 
# 
# 示例 1：
# 
# 输入：grid = [[-1,-2,-3],
# [-2,-3,-3],
# [-3,-3,-2]]
# 输出：-1
# 解释：从 (0, 0) 到 (2, 2) 的路径中无法得到非负积，所以返回 -1
# 
# 
# 示例 2：
# 
# 输入：grid = [[1,-2,1],
# [1,-2,1],
# [3,-4,1]]
# 输出：8
# 解释：最大非负积对应的路径已经用粗体标出 (1 * 1 * -2 * -4 * 1 = 8)
# 
# 
# 示例 3：
# 
# 输入：grid = [[1, 3],
# [0,-4]]
# 输出：0
# 解释：最大非负积对应的路径已经用粗体标出 (1 * 0 * -4 = 0)
# 
# 
# 示例 4：
# 
# 输入：grid = [[ 1, 4,4,0],
# [-2, 0,0,1],
# [ 1,-1,1,1]]
# 输出：2
# 解释：最大非负积对应的路径已经用粗体标出 (1 * -2 * 1 * -1 * 1 * 1 = 2)
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= rows, cols <= 15
# -4 <= grid[i][j] <= 4
# 
# 
#

# @lc code=start
MODULO = 10 ** 9 + 7


def modulo(a: int) -> int:
    if a >= 0:
        return a % MODULO
    return a % MODULO - MODULO


class Solution:
    def maxProductPath(self, grid: list[list[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        dp_max = [[0 for _ in range(cols)] for __ in range(rows)]
        dp_min = [[0 for _ in range(cols)] for __ in range(rows)]

        for i in range(rows):
            for j in range(cols):
                n = grid[i][j]

                if i == 0 and j == 0:
                    dp_max[i][j] = n
                    dp_min[i][j] = n

                elif i == 0:
                    dp_max[i][j] = n * dp_max[i][j - 1]
                    dp_min[i][j] = n * dp_min[i][j - 1]

                elif j == 0:
                    dp_max[i][j] = n * dp_max[i - 1][j]
                    dp_min[i][j] = n * dp_min[i - 1][j]

                elif n > 0:
                    dp_max[i][j] = max(dp_max[i - 1][j], dp_max[i][j - 1]) * n
                    dp_min[i][j] = min(dp_min[i - 1][j], dp_min[i][j - 1]) * n

                else:
                    dp_max[i][j] = min(dp_min[i - 1][j], dp_min[i][j - 1]) * n
                    dp_min[i][j] = max(dp_max[i - 1][j], dp_max[i][j - 1]) * n

                # dp_max[i][j] = modulo(dp_max[i][j])
                # dp_min[i][j] = modulo(dp_min[i][j])

        # print(dp_max)
        return modulo(max(-1, dp_max[-1][-1]))
# @lc code=end

s = Solution()
print(s.maxProductPath([[-1,-2,-3], [-2,-3,-3], [-3,-3,-2]]))
print(s.maxProductPath([[1,-2,1], [1,-2,1], [3,-4,1]]))
print(s.maxProductPath([[1, 3], [0,-4]]))
print(s.maxProductPath([[ 1, 4,4,0], [-2, 0,0,1], [ 1,-1,1,1]]))

# 31136867
print(s.maxProductPath([
    [1,-1,0,-3,4,3,-3,3,-1,3,0,0,-4,2],
    [2,-2,-3,-4,0,-2,-3,3,1,4,1,-3,-1,-4],
    [-4,4,-4,-4,2,-4,3,0,-2,-4,3,4,-1,0],
    [-3,3,-4,-4,3,4,4,1,-1,-1,0,3,4,1],
    [1,3,-4,2,2,-3,1,-3,-4,-4,-1,-4,-4,4],
    [1,1,-1,1,-1,-1,3,-4,-1,2,-2,3,-4,0],
    [1,0,3,3,1,4,1,1,-4,-1,-3,4,-4,4],
    [4,3,2,3,0,-1,2,-4,1,0,0,1,3,4],
    [-4,4,-4,-4,2,-2,2,-1,0,-2,2,4,-2,-1],
    [-2,3,4,-4,3,3,-2,-1,0,-3,4,-2,-1,-4],
    [4,3,3,3,-3,1,2,-4,-1,4,-3,-3,2,0],
    [3,3,0,1,-4,-4,-3,3,-2,-4,2,4,-3,3],
    [-3,0,1,3,0,0,0,-4,-1,4,-1,-3,1,1],
    [-1,4,0,-3,1,-3,-1,2,1,-3,-1,-4,4,1]
]))
