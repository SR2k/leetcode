/*
 * @lc app=leetcode.cn id=54 lang=typescript
 *
 * [54] 螺旋矩阵
 *
 * https://leetcode.cn/problems/spiral-matrix/description/
 *
 * algorithms
 * Medium (49.09%)
 * Likes:    1180
 * Dislikes: 0
 * Total Accepted:    297.1K
 * Total Submissions: 605.2K
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

export
// @lc code=start
function spiralOrder(matrix: number[][]): number[] {
  const result: number[] = []
  const m = matrix.length, n = matrix[0]?.length
  if (!m || !n) {
    return result
  }

  const DIRECTIONS = [[0, 1], [1, 0], [0, -1], [-1, 0]]

  const edges = [n - 1, m - 1, 0, 0]
  const edgeMove = [-1, -1, 1, 1]

  let d = 0
  let i = 0
  let j = 0
  while (result.length < m * n) {
    const e = i * Math.abs(DIRECTIONS[d][0]) + j * Math.abs(DIRECTIONS[d][1])
    if (e === edges[d]) {
      const prevD = (d - 1 + 4) % 4
      edges[prevD] += edgeMove[prevD]
      d = (d + 1) % 4
    }

    result.push(matrix[i][j])

    const [di, dj] = DIRECTIONS[d]
    i += di
    j += dj
  }

  return result
}
// @lc code=end
