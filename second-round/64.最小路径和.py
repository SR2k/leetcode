#
# @lc app=leetcode.cn id=64 lang=python3
#
# [64] 最小路径和
#
# https://leetcode-cn.com/problems/minimum-path-sum/description/
#
# algorithms
# Medium (69.00%)
# Likes:    1119
# Dislikes: 0
# Total Accepted:    303K
# Total Submissions: 439.1K
# Testcase Example:  '[[1,3,1],[1,5,1],[4,2,1]]'
#
# 给定一个包含非负整数的 m x n 网格 grid ，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。
# 
# 说明：每次只能向下或者向右移动一步。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：grid = [[1,3,1],[1,5,1],[4,2,1]]
# 输出：7
# 解释：因为路径 1→3→1→1→1 的总和最小。
# 
# 
# 示例 2：
# 
# 
# 输入：grid = [[1,2,3],[4,5,6]]
# 输出：12
# 
# 
# 
# 
# 提示：
# 
# 
# m == grid.length
# n == grid[i].length
# 1 
# 0 
# 
# 
#

# @lc code=start
class Solution:
    def minPathSum(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = [0 for _ in range(n)]

        for i in range(m):
            for j in range(n):
                if i == 0:
                    dp[j] = dp[j - 1] + grid[i][j]
                elif j == 0:
                    dp[j] = dp[j] + grid[i][j]
                else:
                    dp[j] = min(dp[j - 1], dp[j]) + grid[i][j]

        return dp[-1]
# @lc code=end

s = Solution()
print(s.minPathSum([[1,3,1],[1,5,1],[4,2,1]]))
print(s.minPathSum([[1,2,3],[4,5,6]]))
print(s.minPathSum([[1,1,1],[9,99,1],[1,1,9],[1,1,1]]))
