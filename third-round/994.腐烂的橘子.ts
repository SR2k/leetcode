/*
 * @lc app=leetcode.cn id=994 lang=typescript
 *
 * [994] 腐烂的橘子
 *
 * https://leetcode-cn.com/problems/rotting-oranges/description/
 *
 * algorithms
 * Medium (51.24%)
 * Likes:    496
 * Dislikes: 0
 * Total Accepted:    68.8K
 * Total Submissions: 134.3K
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
  const m = grid.length
  const n = grid[0].length

  const queue: Array<[number, number]> = []
  const rotten: Set<string> = new Set()
  let freshCount = 0
  let result = 0

  grid.forEach((row, i) => {
    row.forEach((cell, j) => {
      if (cell === OrangeStatus.Fresh) {
        freshCount++
      } else if (cell === OrangeStatus.Rotten) {
        queue.push([i, j])
        rotten.add(`${i},${j}`)
      }
    })
  })
  const initialRottenCount = rotten.size

  if (!freshCount) return 0

  while (queue.length) {
    const levelLength = queue.length
    result++

    for (let i = 0; i < levelLength; i++) {
      const [prevI, prevJ] = queue.shift()!

      for (const [di, dj] of DIRECTIONS) {
        const nextI = di + prevI
        const nextJ = dj + prevJ

        if (nextI < 0 || nextI >= m || nextJ < 0 || nextJ >= n) continue
        if (grid[nextI][nextJ] !== OrangeStatus.Fresh) continue
        const resp = `${nextI},${nextJ}`
        if (rotten.has(resp)) continue

        rotten.add(resp)
        queue.push([nextI, nextJ])
      }
    }
  }

  if (rotten.size - initialRottenCount < freshCount) {
    return -1
  }
  return result - 1
}

const DIRECTIONS = [[0, 1], [0, -1], [1, 0], [-1, 0]]

const enum OrangeStatus {
  Empty,
  Fresh,
  Rotten,
}
// @lc code=end
