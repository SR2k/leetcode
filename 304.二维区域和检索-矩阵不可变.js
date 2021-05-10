/*
 * @lc app=leetcode.cn id=304 lang=javascript
 *
 * [304] 二维区域和检索 - 矩阵不可变
 *
 * https://leetcode-cn.com/problems/range-sum-query-2d-immutable/description/
 *
 * algorithms
 * Medium (54.46%)
 * Likes:    266
 * Dislikes: 0
 * Total Accepted:    53.2K
 * Total Submissions: 97.8K
 * Testcase Example:  '["NumMatrix","sumRegion","sumRegion","sumRegion"]\n' +
  '[[[[3,0,1,4,2],[5,6,3,2,1],[1,2,0,1,5],[4,1,0,1,7],[1,0,3,0,5]]],[2,1,4,3],[1,1,2,2],[1,2,2,4]]'
 *
 * 给定一个二维矩阵，计算其子矩形范围内元素的总和，该子矩阵的左上角为 (row1, col1) ，右下角为 (row2, col2) 。
 * 
 * 
 * 上图子矩阵左上角 (row1, col1) = (2, 1) ，右下角(row2, col2) = (4, 3)，该子矩形内元素的总和为 8。
 * 
 * 
 * 
 * 示例：
 * 
 * 
 * 给定 matrix = [
 * ⁠ [3, 0, 1, 4, 2],
 * ⁠ [5, 6, 3, 2, 1],
 * ⁠ [1, 2, 0, 1, 5],
 * ⁠ [4, 1, 0, 1, 7],
 * ⁠ [1, 0, 3, 0, 5]
 * ]
 * 
 * sumRegion(2, 1, 4, 3) -> 8
 * sumRegion(1, 1, 2, 2) -> 11
 * sumRegion(1, 2, 2, 4) -> 12
 * 
 * 
 * 
 * 
 * 提示：
 * 
 * 
 * 你可以假设矩阵不可变。
 * 会多次调用 sumRegion 方法。
 * 你可以假设 row1 ≤ row2 且 col1 ≤ col2 。
 * 
 * 
 */

// @lc code=start
/**
 * @param {number[][]} matrix
 */
var NumMatrix = function (matrix) {
  const prefixSum = [];
  this.prefixSum = prefixSum;

  const m = matrix.length;
  const n = matrix[0].length;

  for (let i = 0; i < m; i++) {
    prefixSum[i] = [];

    for (let j = 0; j < n; j++) {
      if (i === 0 && j === 0) {
        prefixSum[i][j] = matrix[i][j];
      } else if (i === 0) {
        prefixSum[i][j] = prefixSum[i][j - 1] + matrix[i][j];
      } else if (j === 0) {
        prefixSum[i][j] = prefixSum[i - 1][j] + matrix[i][j];
      } else {
        prefixSum[i][j] =
          prefixSum[i - 1][j] +
          prefixSum[i][j - 1] -
          prefixSum[i - 1][j - 1] +
          matrix[i][j];
      }
    }
  }
};

/**
 * @param {number} row1
 * @param {number} col1
 * @param {number} row2
 * @param {number} col2
 * @return {number}
 */
NumMatrix.prototype.sumRegion = function (row1, col1, row2, col2) {
  // edge cases
  if (!this.prefixSum.length) return 0;
  if (!this.prefixSum[0].length) return 0;

  // normalize
  if (row1 < 0) row1 = 0;
  if (col1 < 0) col1 = 0;
  if (row2 >= this.prefixSum.length) row2 = this.prefixSum.length - 1;
  if (col2 >= this.prefixSum[0].length) col2 = this.prefixSum[0].length - 1;

  // do the calculate
  if (row1 === 0 && col1 === 0) {
    return this.prefixSum[row2][col2];
  }
  if (row1 === 0) {
    return this.prefixSum[row2][col2] - this.prefixSum[row2][col1 - 1];
  }
  if (col1 === 0) {
    return this.prefixSum[row2][col2] - this.prefixSum[row1 - 1][col2];
  }
  return (
    this.prefixSum[row2][col2] -
    this.prefixSum[row1 - 1][col2] -
    this.prefixSum[row2][col1 - 1] +
    this.prefixSum[row1 - 1][col1 - 1]
  );
};

/**
 * Your NumMatrix object will be instantiated and called as such:
 * var obj = new NumMatrix(matrix)
 * var param_1 = obj.sumRegion(row1,col1,row2,col2)
 */
// @lc code=end

// var obj = new NumMatrix(
//   [
//     [3, 0, 1, 4, 2],
//     [5, 6, 3, 2, 1],
//     [1, 2, 0, 1, 5],
//     [4, 1, 0, 1, 7],
//     [1, 0, 3, 0, 5]
//   ]
// )
// console.log(obj.sumRegion(2, 1, 4, 3))
// console.log(obj.sumRegion(1, 1, 2, 2))
// console.log(obj.sumRegion(1, 2, 2, 4))
// console.log(obj.sumRegion(0, 0, 2, 4))
// console.log(obj.sumRegion(0, 1, 2, 4))
// console.log(obj.sumRegion(1, 0, 2, 4))
