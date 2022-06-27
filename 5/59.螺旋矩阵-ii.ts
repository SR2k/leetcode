/*
 * @lc app=leetcode.cn id=59 lang=typescript
 *
 * [59] 螺旋矩阵 II
 *
 * https://leetcode.cn/problems/spiral-matrix-ii/description/
 *
 * algorithms
 * Medium (76.26%)
 * Likes:    728
 * Dislikes: 0
 * Total Accepted:    204.5K
 * Total Submissions: 268.2K
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
  let d = 0
  const edges = [n - 1, n - 1, 0, 0]

  const result = new Array(n).fill(0).map(() => (
    new Array(n).fill(0)
  ))

  let i = 0, j = 0
  for (let x = 1; x <= n * n; x++) {
    result[i][j] = x

    const [di, dj] = DIRECTIONS[d]
    i += di
    j += dj

    switch (d) {
      case 0:
        if (j === edges[d]) {
          edges[3] += 1
          d += 1
        }
        break
      case 1:
        if (i === edges[d]) {
          edges[0] -= 1
          d += 1
        }
        break
      case 2:
        if (j === edges[d]) {
          edges[1] -= 1
          d += 1
        }
        break
      case 3:
        if (i === edges[d]) {
          edges[2] += 1
          d = 0
        }
    }
  }

  return result
}

const DIRECTIONS = [[0, 1], [1, 0], [0, -1], [-1, 0]]
// @lc code=end
