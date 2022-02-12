/*
 * @lc app=leetcode.cn id=200 lang=typescript
 *
 * [200] 岛屿数量
 *
 * https://leetcode-cn.com/problems/number-of-islands/description/
 *
 * algorithms
 * Medium (56.18%)
 * Likes:    1434
 * Dislikes: 0
 * Total Accepted:    359.8K
 * Total Submissions: 640.5K
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
  let result = 0
  const visited: boolean[][] = new Array(grid.length).fill(0).map(() => new Array(grid[0].length).fill(false))

  grid.forEach((row, i) => {
    row.forEach((_, j) => {
      if (helper(grid, visited, i, j)) {
        result += 1
      }
    })
  })

  return result
}

const DIRECTIONS = [[0, 1], [0, -1], [1, 0], [-1, 0]]

function helper(grid: string[][], visited: boolean[][], i: number, j: number): boolean {
  if (!(i >= 0 && i < grid.length && j >= 0 && j < grid[0].length)) {
    return false
  }
  if (visited[i][j]) {
    return false
  }
  visited[i][j] = true

  if (grid[i][j] !== Grid.Island) {
    return false
  }

  for (const [di, dj] of DIRECTIONS) {
    helper(grid, visited, i + di, j + dj)
  }

  return true
}

const enum Grid {
  Island = '1',
  Ocean = '0',
}
// @lc code=end
