/*
 * @lc app=leetcode.cn id=59 lang=typescript
 *
 * [59] 螺旋矩阵 II
 *
 * https://leetcode.cn/problems/spiral-matrix-ii/description/
 *
 * algorithms
 * Medium (75.61%)
 * Likes:    815
 * Dislikes: 0
 * Total Accepted:    240.3K
 * Total Submissions: 318.8K
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

export
// @lc code=start
function generateMatrix(n: number): number[][] {
  const result = new Array(n).fill(0)
    .map(() => new Array<number>(n).fill(0))

  let i = 0, j = 0
  let filled = 1
  let d = 0

  const edges = [n - 1, n - 1, 0, 0]

  while (filled <= n * n) {
    result[i][j] = filled++

    const [di, dj] = DIRECTIONS[d]
    i += di
    j += dj

    const e = Math.abs(i * di) + Math.abs(j * dj)
    if (e === edges[d]) {
      const prev = (d - 1 + 4) % 4
      const [pi, pj] = DIRECTIONS[prev]
      edges[prev] -= Math.abs(pi) > Math.abs(pj) ? pi : pj
      d = (d + 1) % 4
    }
  }

  return result
}

const DIRECTIONS = [[0, 1], [1, 0], [0, -1], [-1, 0]]
// @lc code=end
