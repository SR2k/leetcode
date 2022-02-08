#
# @lc app=leetcode.cn id=54 lang=python3
#
# [54] 螺旋矩阵
#
# https://leetcode-cn.com/problems/spiral-matrix/description/
#
# algorithms
# Medium (48.34%)
# Likes:    963
# Dislikes: 0
# Total Accepted:    214.4K
# Total Submissions: 443.5K
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


class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        m, n = len(matrix), len(matrix[0])

        result = []
        i, j = 0, 0
        top, bottom, left, right = 0, m - 1, 0, n - 1
        d = 0

        while len(result) < m * n:
            result.append(matrix[i][j])

            if d == 0 and j == right:
                d += 1
                top += 1
            elif d == 1 and i == bottom:
                d += 1
                right -= 1
            elif d == 2 and j == left:
                d += 1
                bottom -= 1
            elif d == 3 and i == top:
                d += 1
                left += 1
            d %= 4

            i += DIRECTIONS[d][0]
            j += DIRECTIONS[d][1]

        return result
# @lc code=end

s = Solution()
print(s.spiralOrder([[1,2,3],[4,5,6],[7,8,9]]))
print(s.spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12]]))
