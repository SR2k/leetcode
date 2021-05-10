/*
 * @lc app=leetcode.cn id=59 lang=javascript
 *
 * [59] 螺旋矩阵 II
 *
 * https://leetcode-cn.com/problems/spiral-matrix-ii/description/
 *
 * algorithms
 * Medium (79.86%)
 * Likes:    416
 * Dislikes: 0
 * Total Accepted:    100.5K
 * Total Submissions: 125.9K
 * Testcase Example:  '3'
 *
 * 给你一个正整数 n ，生成一个包含 1 到 n^2 所有元素，且元素按顺时针顺序螺旋排列的 n x n 正方形矩阵 matrix 。
 * 
 * 
 * 
 * 示例 1：
 * 
 * 
 * 输入：n = 3
 * 输出：[[1,2,3],[8,9,4],[7,6,5]]
 * 
 * 
 * 示例 2：
 * 
 * 
 * 输入：n = 1
 * 输出：[[1]]
 * 
 * 
 * 
 * 
 * 提示：
 * 
 * 
 * 1 
 * 
 * 
 */

// @lc code=start
/**
 * @param {number} n
 * @return {number[][]}
 */
var generateMatrix = function(n) {
  if (n === 0) return []
  let topBoundary = 0, leftBoundary = 0, bottomBoundary = n - 1, rightBoundary = n - 1

  let i = 0, j = -1, direction = 'r', count = 0
  const result = []

  while (true) {
    if (count === n * n) return result

    switch (direction) {
      case 't': i--; break
      case 'b': i++; break
      case 'l': j--; break
      case 'r': j++; break
    }

    count++
    if (!result[i]) result[i] = []
    result[i][j] = count

    if (direction === 'r' && j === rightBoundary) {
      topBoundary ++
      direction = 'b'
    } else if (direction === 'b' && i === bottomBoundary) {
      rightBoundary --
      direction = 'l'
    } else if (direction === 'l' && j === leftBoundary) {
      bottomBoundary --
      direction = 't'
    } else if (direction === 't' && i === topBoundary) {
      leftBoundary ++
      direction = 'r'
    }
  }
};
// @lc code=end
