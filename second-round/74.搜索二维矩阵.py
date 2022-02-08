#
# @lc app=leetcode.cn id=74 lang=python3
#
# [74] 搜索二维矩阵
#
# https://leetcode-cn.com/problems/search-a-2d-matrix/description/
#
# algorithms
# Medium (46.69%)
# Likes:    561
# Dislikes: 0
# Total Accepted:    195.5K
# Total Submissions: 418.5K
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
    @staticmethod
    def index_to_twod(index: int, line_cnt: int) -> tuple[int, int]:
        i = index // line_cnt
        j = index % line_cnt
        return i, j

    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        left, right = 0, m * n - 1

        while left + 1 < right:
            middle = (left + right) // 2
            i, j = Solution.index_to_twod(middle, n)
            num_middle = matrix[i][j]

            if num_middle == target:
                return True
            elif num_middle > target:
                right = middle
            else:
                left = middle

        i, j = Solution.index_to_twod(left, n)
        if matrix[i][j] == target:
            return True
        i, j = Solution.index_to_twod(right, n)
        if matrix[i][j] == target:
            return True
        return False
# @lc code=end

s = Solution()
print(s.searchMatrix([[1,1]], 0))
