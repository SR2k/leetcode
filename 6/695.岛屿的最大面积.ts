/*
 * @lc app=leetcode.cn id=695 lang=typescript
 *
 * [695] 岛屿的最大面积
 *
 * https://leetcode.cn/problems/max-area-of-island/description/
 *
 * algorithms
 * Medium (67.69%)
 * Likes:    802
 * Dislikes: 0
 * Total Accepted:    216.1K
 * Total Submissions: 319.2K
 * Testcase Example:  '[[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]'
 *
 * 给你一个大小为 m x n 的二进制矩阵 grid 。
 *
 * 岛屿 是由一些相邻的 1 (代表土地) 构成的组合，这里的「相邻」要求两个 1 必须在 水平或者竖直的四个方向上 相邻。你可以假设 grid
 * 的四个边缘都被 0（代表水）包围着。
 *
 * 岛屿的面积是岛上值为 1 的单元格的数目。
 *
 * 计算并返回 grid 中最大的岛屿面积。如果没有岛屿，则返回面积为 0 。
 *
 *
 *
 * 示例 1：
 *
 *
 * 输入：grid =
 * [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
 * 输出：6
 * 解释：答案不应该是 11 ，因为岛屿只能包含水平或垂直这四个方向上的 1 。
 *
 *
 * 示例 2：
 *
 *
 * 输入：grid = [[0,0,0,0,0,0,0,0]]
 * 输出：0
 *
 *
 *
 *
 * 提示：
 *
 *
 * m == grid.length
 * n == grid[i].length
 * 1 <= m, n <= 50
 * grid[i][j] 为 0 或 1
 *
 *
 */

export
// @lc code=start
function maxAreaOfIsland(grid: number[][]): number {
  type Point = [number, number]

  const m = grid.length, n = grid[0].length;

  function walk(i: number, j: number) {
    if (grid[i][j] !== GridTypes.Land) {
      return 0
    }

    let size = 0
    const queue: Point[] = [[i, j]]
    grid[i][j] = GridTypes.Ocean

    while (queue.length) {
      const [i, j] = queue.shift()!
      size++

      for (const [ni, nj] of moves(i, j, m, n)) {
        if (grid[ni][nj] === GridTypes.Land) {
          grid[ni][nj] = GridTypes.Ocean
          queue.push([ni, nj])
        }
      }
    }

    return size
  }

  let result = 0
  for (let i = 0; i < m; i++) {
    for (let j = 0; j < n; j++) {
      result = Math.max(walk(i, j), result)
    }
  }

  return result
}

const enum GridTypes {
  Ocean,
  Land,
}

const DIRECTIONS = [[0, 1], [0, -1], [1, 0], [-1, 0]]

function* moves(i: number, j: number, m: number, n: number) {
  for (const [di, dj] of DIRECTIONS) {
    const ni = i + di, nj = j + dj
    if (ni < 0 || ni >= m || nj < 0 || nj >= n) continue
    yield [ni, nj]
  }
}
// @lc code=end
