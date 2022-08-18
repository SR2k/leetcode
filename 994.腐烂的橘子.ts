/*
 * @lc app=leetcode.cn id=994 lang=typescript
 *
 * [994] 腐烂的橘子
 *
 * https://leetcode.cn/problems/rotting-oranges/description/
 *
 * algorithms
 * Medium (51.08%)
 * Likes:    587
 * Dislikes: 0
 * Total Accepted:    91.6K
 * Total Submissions: 179.4K
 * Testcase Example:  '[[2,1,1],[1,1,0],[0,1,1]]'
 *
 * 在给定的 m x n 网格 grid 中，每个单元格可以有以下三个值之一：
 *
 *
 * 值 0 代表空单元格；
 * 值 1 代表新鲜橘子；
 * 值 2 代表腐烂的橘子。
 *
 *
 * 每分钟，腐烂的橘子 周围 4 个方向上相邻 的新鲜橘子都会腐烂。
 *
 * 返回 直到单元格中没有新鲜橘子为止所必须经过的最小分钟数。如果不可能，返回 -1 。
 *
 *
 *
 * 示例 1：
 *
 *
 *
 *
 * 输入：grid = [[2,1,1],[1,1,0],[0,1,1]]
 * 输出：4
 *
 *
 * 示例 2：
 *
 *
 * 输入：grid = [[2,1,1],[0,1,1],[1,0,1]]
 * 输出：-1
 * 解释：左下角的橘子（第 2 行， 第 0 列）永远不会腐烂，因为腐烂只会发生在 4 个正向上。
 *
 *
 * 示例 3：
 *
 *
 * 输入：grid = [[0,2]]
 * 输出：0
 * 解释：因为 0 分钟时已经没有新鲜橘子了，所以答案就是 0 。
 *
 *
 *
 *
 * 提示：
 *
 *
 * m == grid.length
 * n == grid[i].length
 * 1 <= m, n <= 10
 * grid[i][j] 仅为 0、1 或 2
 *
 *
 */

export
// @lc code=start
function orangesRotting(grid: number[][]): number {
  const queue: Array<[number, number]> = []
  let freshCount = 0
  grid.forEach((row, i) => {
    row.forEach((cell, j) => {
      if (cell === CellStatus.Fresh) {
        freshCount++
      } else if (cell === CellStatus.Rotten) {
        queue.push([i, j])
      }
    })
  })

  if (!freshCount) return 0

  const m = grid.length, n = grid[0].length

  let result = 0
  while (freshCount && queue.length) {
    result++
    const levelResult = queue.length

    for (let x = 0; x < levelResult; x++) {
      const [i, j] = queue.shift()!

      for (const [di, dj] of Directions) {
        const ni = i + di, nj = j + dj
        if (ni < 0 || ni >= m || nj < 0 || nj >= n) continue

        if (grid[ni][nj] === CellStatus.Fresh) {
          grid[ni][nj] = CellStatus.Rotten
          freshCount--
          queue.push([ni, nj])
        }
      }
    }
  }

  if (freshCount) return -1
  return result
}

const enum CellStatus {
  Empty,
  Fresh,
  Rotten,
}

const Directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
// @lc code=end
