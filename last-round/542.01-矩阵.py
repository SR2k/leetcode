#
# @lc app=leetcode.cn id=542 lang=python3
#
# [542] 01 矩阵
#
# https://leetcode-cn.com/problems/01-matrix/description/
#
# algorithms
# Medium (45.68%)
# Likes:    442
# Dislikes: 0
# Total Accepted:    54.3K
# Total Submissions: 118.7K
# Testcase Example:  '[[0,0,0],[0,1,0],[0,0,0]]'
#
# 给定一个由 0 和 1 组成的矩阵，找出每个元素到最近的 0 的距离。
# 
# 两个相邻元素间的距离为 1 。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：
# [[0,0,0],
# ⁠[0,1,0],
# ⁠[0,0,0]]
# 
# 输出：
# [[0,0,0],
# [0,1,0],
# [0,0,0]]
# 
# 
# 示例 2：
# 
# 
# 输入：
# [[0,0,0],
# ⁠[0,1,0],
# ⁠[1,1,1]]
# 
# 输出：
# [[0,0,0],
# ⁠[0,1,0],
# ⁠[1,2,1]]
# 
# 
# 
# 
# 提示：
# 
# 
# 给定矩阵的元素个数不超过 10000。
# 给定矩阵中至少有一个元素是 0。
# 矩阵中的元素只在四个方向上相邻: 上、下、左、右。
# 
# 
#

# @lc code=start
class Solution:
    def updateMatrix(self, mat: list[list[int]]) -> list[list[int]]:
        m, n = len(mat), len(mat[0])
        dp_top_left = [[0 for _ in range(n)] for __ in range(m)]

        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    continue
                temp = []
                if i - 1 >= 0: temp.append(dp_top_left[i - 1][j])
                if j - 1 >= 0: temp.append(dp_top_left[i][j - 1])
                dp_top_left[i][j] = min(temp) + 1 if temp else m + n + 1

        ret = [[0 for _ in range(n)] for __ in range(m)]
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if mat[i][j] == 0:
                    continue
                temp = [dp_top_left[i][j]]
                if i + 1 < m: temp.append(ret[i + 1][j] + 1)
                if j + 1 < n: temp.append(ret[i][j + 1] + 1)
                ret[i][j] = min(temp)

        return ret
# @lc code=end

