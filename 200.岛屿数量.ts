/*
 * @lc app=leetcode.cn id=200 lang=typescript
 *
 * [200] 岛屿数量
 *
 * https://leetcode.cn/problems/number-of-islands/description/
 *
 * algorithms
 * Medium (58.42%)
 * Likes:    1851
 * Dislikes: 0
 * Total Accepted:    532.6K
 * Total Submissions: 911.6K
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
const enum GridType {
  Ocean = '0',
  Land = '1',
}

const DIRECTIONS = [[0, 1], [0, -1], [1, 0], [-1, 0]]

function numIslands(grid: string[][]): number {
  const m = grid.length, n = grid[0]?.length
  if (!m || !n) return 0

  const walk = (i: number, j: number) => {
    if (i < 0 || i >= m || j < 0 || j >= n) return 0
    if (grid[i][j] !== GridType.Land) return 0

    grid[i][j] = GridType.Ocean
    DIRECTIONS.forEach(([di, dj]) => walk(i + di, j + dj))

    return 1
  }

  let result = 0
  for (let i = 0; i < m; i++) {
    for (let j = 0; j < n; j++) {
      result += walk(i, j)
    }
  }

  return result
}
// @lc code=end
