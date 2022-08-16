/*
 * @lc app=leetcode.cn id=54 lang=typescript
 *
 * [54] 螺旋矩阵
 *
 * https://leetcode.cn/problems/spiral-matrix/description/
 *
 * algorithms
 * Medium (48.81%)
 * Likes:    1118
 * Dislikes: 0
 * Total Accepted:    269.7K
 * Total Submissions: 552.5K
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
  const m = matrix.length, n = matrix[0].length

  const edges = [0, n - 1, m - 1, 0]
  const directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
  const masks = [[0, 1], [1, 0], [0, 1], [1, 0]]
  const edgeMoves = [1, -1, -1, 1]
  const result: number[] = []

  let i = 0, j = 0
  let d = 0

  while (result.length < m * n) {
    result.push(matrix[i][j])

    const nextD = (d + 1) % edges.length
    const [maskI, maskJ] = masks[d]
    if (i * maskI + j * maskJ === edges[nextD]) {
      edges[d] += edgeMoves[d]
      d = nextD
    }

    const [di, dj] = directions[d]
    i += di
    j += dj
  }

  return result
}
// @lc code=end
