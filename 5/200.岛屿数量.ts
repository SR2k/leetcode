/*
 * @lc app=leetcode.cn id=200 lang=typescript
 *
 * [200] 岛屿数量
 *
 * https://leetcode.cn/problems/number-of-islands/description/
 *
 * algorithms
 * Medium (57.90%)
 * Likes:    1769
 * Dislikes: 0
 * Total Accepted:    494.6K
 * Total Submissions: 852.8K
 * Testcase Example:  '[["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]'
 *
 * 给你一个由 '1'（陆地）和 '0'（水）组成的的二维网格，请你计算网格中岛屿的数量。
 *
 * 岛屿总是被水包围，并且每座岛屿只能由水平方向和/或竖直方向上相邻的陆地连接形成。
 *
 * 此外，你可以假设该网格的四条边均被水包围。
 *
 *
 *
 * 示例 1：
 *
 *
 * 输入：grid = [
 * ⁠ ["1","1","1","1","0"],
 * ⁠ ["1","1","0","1","0"],
 * ⁠ ["1","1","0","0","0"],
 * ⁠ ["0","0","0","0","0"]
 * ]
 * 输出：1
 *
 *
 * 示例 2：
 *
 *
 * 输入：grid = [
 * ⁠ ["1","1","0","0","0"],
 * ⁠ ["1","1","0","0","0"],
 * ⁠ ["0","0","1","0","0"],
 * ⁠ ["0","0","0","1","1"]
 * ]
 * 输出：3
 *
 *
 *
 *
 * 提示：
 *
 *
 * m == grid.length
 * n == grid[i].length
 * 1
 * grid[i][j] 的值为 '0' 或 '1'
 *
 *
 */

export
// @lc code=start
function numIslands(grid: string[][]): number {
  const m = grid.length, n = grid[0].length

  const walk = (i: number, j: number): boolean => {
    if (i < 0 || i >= m || j < 0 || j >= n) {
      return false
    }
    if (grid[i][j] !== LAND) {
      return false
    }

    grid[i][j] = WATER

    DIRECTIONS.forEach(([di, dj]) => {
      walk(i + di, j + dj)
    })
    return true
  }

  let result = 0
  for (let i = 0; i < m; i++) {
    for (let j = 0; j < n; j++) {
      if (walk(i, j)) {
        result++
      }
    }
  }

  return result
}

const LAND = '1', WATER = '0'
const DIRECTIONS = [[0, 1], [0, -1], [1, 0], [-1, 0]]
// @lc code=end
