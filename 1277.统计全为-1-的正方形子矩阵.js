/*
 * @lc app=leetcode.cn id=1277 lang=javascript
 *
 * [1277] 统计全为 1 的正方形子矩阵
 *
 * https://leetcode-cn.com/problems/count-square-submatrices-with-all-ones/description/
 *
 * algorithms
 * Medium (72.05%)
 * Likes:    149
 * Dislikes: 0
 * Total Accepted:    15.5K
 * Total Submissions: 21.5K
 * Testcase Example:  '[[0,1,1,1],[1,1,1,1],[0,1,1,1]]'
 *
 * 给你一个 m * n 的矩阵，矩阵中的元素不是 0 就是 1，请你统计并返回其中完全由 1 组成的 正方形 子矩阵的个数。
 * 
 * 
 * 
 * 示例 1：
 * 
 * 输入：matrix =
 * [
 * [0,1,1,1],
 * [1,1,1,1],
 * [0,1,1,1]
 * ]
 * 输出：15
 * 解释： 
 * 边长为 1 的正方形有 10 个。
 * 边长为 2 的正方形有 4 个。
 * 边长为 3 的正方形有 1 个。
 * 正方形的总数 = 10 + 4 + 1 = 15.
 * 
 * 
 * 示例 2：
 * 
 * 输入：matrix = 
 * [
 * ⁠ [1,0,1],
 * ⁠ [1,1,0],
 * ⁠ [1,1,0]
 * ]
 * 输出：7
 * 解释：
 * 边长为 1 的正方形有 6 个。 
 * 边长为 2 的正方形有 1 个。
 * 正方形的总数 = 6 + 1 = 7.
 * 
 * 
 * 
 * 
 * 提示：
 * 
 * 
 * 1 <= arr.length <= 300
 * 1 <= arr[0].length <= 300
 * 0 <= arr[i][j] <= 1
 * 
 * 
 */

// @lc code=start
/**
 * @param {number[][]} matrix
 * @return {number}
 */
var countSquares = function(matrix) {
  const m = matrix.length
  if (!m) return 0
  const n = matrix[0].length
  if (!n) return 0

  const dp = []
  let sum = 0
  for (let i = 0; i < m; i++) {
    dp[i] = []

    for (let j = 0; j < n; j++) {
      if (i === 0 || j === 0) {
        dp[i][j] = matrix[i][j]
      } else if (matrix[i][j]) {
        dp[i][j] = 1 + Math.min(
          dp[i - 1][j],
          dp[i][j - 1],
          dp[i - 1][j - 1],
        )
      } else {
        dp[i][j] = 0
      }

      sum += dp[i][j]
    }
  }

  return sum
};

// @lc code=end

// console.log(countSquares([]))
// console.log(countSquares([[], []]))

// let testCase = [
//   [1, 0, 1],
//   [1, 1, 0],
//   [1, 1, 0]
// ]

// console.log(countSquares(testCase))
