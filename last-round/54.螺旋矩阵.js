/*
 * @lc app=leetcode.cn id=54 lang=javascript
 *
 * [54] 螺旋矩阵
 *
 * https://leetcode-cn.com/problems/spiral-matrix/description/
 *
 * algorithms
 * Medium (46.78%)
 * Likes:    770
 * Dislikes: 0
 * Total Accepted:    151.4K
 * Total Submissions: 323.5K
 * Testcase Example:  '[[1,2,3],[4,5,6],[7,8,9]]'
 *
 * 给你一个 m 行 n 列的矩阵 matrix ，请按照 顺时针螺旋顺序 ，返回矩阵中的所有元素。
 * 
 * 
 * 
 * 示例 1：
 * 
 * 
 * 输入：matrix = [[1,2,3],[4,5,6],[7,8,9]]
 * 输出：[1,2,3,6,9,8,7,4,5]
 * 
 * 
 * 示例 2：
 * 
 * 
 * 输入：matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
 * 输出：[1,2,3,4,8,12,11,10,9,5,6,7]
 * 
 * 
 * 
 * 
 * 提示：
 * 
 * 
 * m == matrix.length
 * n == matrix[i].length
 * 1 
 * -100 
 * 
 * 
 */

// @lc code=start
/**
 * @param {number[][]} matrix
 * @return {number[]}
 */
var spiralOrder = function(matrix) {
  const m = matrix.length
  if (!m) return []
  const n = matrix[0].length
  if (!n) return []

  let topBoundary = 0
  let bottomBoundary = m - 1
  let leftBoundary = 0
  let rightBoundary = n - 1

  let i = 0, j = -1
  let direction = 'r'
  const result = []

  while (true) {
    // do the move
    switch (direction) {
      case 't': i--; break;
      case 'b': i++; break;
      case 'l': j--; break;
      case 'r': j++; break;
    }

    result.push(matrix[i][j])
    if (result.length === m * n) return result

    if (direction === 'r' && j === rightBoundary) {
      // right move touched the boundary
      topBoundary++
      direction = 'b'
    } else if (direction === 'b' && i === bottomBoundary) {
      rightBoundary--
      direction = 'l'
    } else if (direction === 'l' && j === leftBoundary) {
      bottomBoundary--
      direction = 't'
    } else if (direction === 't' && i === topBoundary) {
      leftBoundary++
      direction = 'r'
    }
  }
};
// @lc code=end
