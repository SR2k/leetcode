/*
 * @lc app=leetcode.cn id=74 lang=typescript
 *
 * [74] 搜索二维矩阵
 *
 * https://leetcode.cn/problems/search-a-2d-matrix/description/
 *
 * algorithms
 * Medium (47.67%)
 * Likes:    673
 * Dislikes: 0
 * Total Accepted:    245.3K
 * Total Submissions: 514.5K
 * Testcase Example:  '[[1,3,5,7],[10,11,16,20],[23,30,34,60]]\n3'
 *
 * 编写一个高效的算法来判断 m x n 矩阵中，是否存在一个目标值。该矩阵具有如下特性：
 *
 *
 * 每行中的整数从左到右按升序排列。
 * 每行的第一个整数大于前一行的最后一个整数。
 *
 *
 *
 *
 * 示例 1：
 *
 *
 * 输入：matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
 * 输出：true
 *
 *
 * 示例 2：
 *
 *
 * 输入：matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
 * 输出：false
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
 * -10^4
 *
 *
 */

export
// @lc code=start
function searchMatrix(matrix: number[][], target: number): boolean {
  const m = matrix.length, n = matrix[0].length
  if (!m || !n) return false

  let left = 0, right = m * n - 1
  while (left + 1 < right) {
    const middle = (left + right) >> 1
    const val = get(matrix, middle)

    if (val === target) {
      return true
    } else if (val > target) {
      right = middle
    } else {
      left = middle
    }
  }

  return get(matrix, left) === target || get(matrix, right) === target
}

function get(matrix: number[][], i: number) {
  const n = matrix[0].length
  const j = i % n
  return matrix[(i - j) / n][j]
}
// @lc code=end
