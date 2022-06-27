#
# @lc app=leetcode.cn id=74 lang=python3
#
# [74] 搜索二维矩阵
#
# https://leetcode.cn/problems/search-a-2d-matrix/description/
#
# algorithms
# Medium (47.55%)
# Likes:    663
# Dislikes: 0
# Total Accepted:    239.2K
# Total Submissions: 502.7K
# Testcase Example:  '[[1,3,5,7],[10,11,16,20],[23,30,34,60]]\n3'
#
# 编写一个高效的算法来判断 m x n 矩阵中，是否存在一个目标值。该矩阵具有如下特性：
# 
# 
# 每行中的整数从左到右按升序排列。
# 每行的第一个整数大于前一行的最后一个整数。
# 
# 
# 
# 
# 示例 1：
# 
# 
# 输入：matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
# 输出：true
# 
# 
# 示例 2：
# 
# 
# 输入：matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
# 输出：false
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
# -10^4 
# 
# 
#

# @lc code=start
class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])

        def value_of(k: int):
            i = k // n
            j = k - i * n
            return matrix[i][j]

        left, right = 0, m * n - 1

        while left + 1 < right:
            middle = (left + right) // 2
            val_middle = value_of(middle)

            if val_middle == target:
                return True
            elif val_middle > target:
                right = middle
            else:
                left = middle

        return value_of(left) == target or value_of(right) == target
# @lc code=end
