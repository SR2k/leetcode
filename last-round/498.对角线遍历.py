#
# @lc app=leetcode.cn id=498 lang=python3
#
# [498] 对角线遍历
#
# https://leetcode-cn.com/problems/diagonal-traverse/description/
#
# algorithms
# Medium (44.42%)
# Likes:    207
# Dislikes: 0
# Total Accepted:    36.4K
# Total Submissions: 81.7K
# Testcase Example:  '[[1,2,3],[4,5,6],[7,8,9]]'
#
# 给定一个含有 M x N 个元素的矩阵（M 行，N 列），请以对角线遍历的顺序返回这个矩阵中的所有元素，对角线遍历如下图所示。
# 
# 
# 
# 示例:
# 
# 输入:
# [
# ⁠[ 1, 2, 3 ],
# ⁠[ 4, 5, 6 ],
# ⁠[ 7, 8, 9 ]
# ]
# 
# 输出:  [1,2,4,7,5,3,6,8,9]
# 
# 解释:
# 
# 
# 
# 
# 
# 说明:
# 
# 
# 给定矩阵中的元素总数不会超过 100000 。
# 
# 
#

# @lc code=start
TOP_RIGHT = (-1, 1)
BOTTOM_LEFT = (1, -1)

class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        m, n = len(mat), len(mat[0])
        direction, entrance = TOP_RIGHT, (0, 0)

        ret = []
        while len(ret) < m * n:
            i, j = entrance
            deltaI, deltaJ = direction

            while True:
                ret.append(mat[i][j])

                if deltaI == TOP_RIGHT[0]:
                    if j == n - 1:
                        entrance = (i + 1, j)
                        break
                    elif i == 0:
                        entrance = (i, j + 1)
                        break
                else:
                    if i == m - 1:
                        entrance = (i, j + 1)
                        break
                    elif j == 0:
                        entrance = (i + 1, j)
                        break

                i += deltaI
                j += deltaJ

            direction = BOTTOM_LEFT if direction == TOP_RIGHT else TOP_RIGHT

        return ret
# @lc code=end

