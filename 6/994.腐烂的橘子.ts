/*
 * @lc app=leetcode.cn id=994 lang=typescript
 *
 * [994] 腐烂的橘子
 *
 * https://leetcode.cn/problems/rotting-oranges/description/
 *
 * algorithms
 * Medium (50.98%)
 * Likes:    567
 * Dislikes: 0
 * Total Accepted:    85.6K
 * Total Submissions: 168K
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
  let orangeCount = 0
  const queue: Point[] = []
  const m = grid.length, n = grid[0].length

  for (let i = 0; i < m; i++) {
    for (let j = 0; j < n; j++) {
      if (grid[i][j] === CellStatus.Fresh) {
        orangeCount++
      } else if (grid[i][j] === CellStatus.Rotten) {
        orangeCount++
        queue.push([i, j])
      }
    }
  }

  if (!orangeCount) return 0

  let days = 0
  let rottenCount = 0

  while (queue.length) {
    days++
    const todayLength = queue.length

    for (let d = 0; d < todayLength; d++) {
      const [i, j] = queue.shift()!
      rottenCount++

      for (const [di, dj] of DIRECTIONS) {
        const ni = i + di, nj = j + dj

        if (ni < 0 || ni >= m || nj < 0 || nj >= n) {
          continue
        }
        if (grid[ni][nj] !== CellStatus.Fresh) {
          continue
        }
        grid[ni][nj] = CellStatus.Rotten
        queue.push([ni, nj])
      }
    }
  }

  if (rottenCount === orangeCount) {
    return days - 1
  }
  return -1
}

type Point = [number, number]

const DIRECTIONS = [[0, 1], [0, -1], [1, 0], [-1, 0]]

const enum CellStatus {
  Empty,
  Fresh,
  Rotten,
}
// @lc code=end
