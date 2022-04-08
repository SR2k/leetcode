/*
 * @lc app=leetcode.cn id=695 lang=typescript
 *
 * [695] 岛屿的最大面积
 *
 * https://leetcode-cn.com/problems/max-area-of-island/description/
 *
 * algorithms
 * Medium (67.08%)
 * Likes:    689
 * Dislikes: 0
 * Total Accepted:    165.7K
 * Total Submissions: 246.9K
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
  let result = 0
  const seen = new Set<string>()
  for (let i = 0; i < grid.length; i++) {
    for (let j = 0; j < grid[0].length; j++) {
      if (grid[i][j] === 1) {
        result = Math.max(result, helper(grid, i, j, seen))
      }
    }
  }
  return result
}

function helper(grid: number[][], i: number, j: number, seen: Set<string>) {
  if (seen.has(`${i},${j}`)) return 0
  seen.add(`${i},${j}`)

  const queue: Array<[number, number]> = [[i, j]]
  let count = 0
  const m = grid.length
  const n = grid[0].length

  while (queue.length) {
    count += 1
    const [prevI, prevJ] = queue.shift()!
    seen.add(`${prevI},${prevJ}`)

    for (const [di, dj] of DIRECTIONS) {
      const nextI = prevI + di
      const nextJ = prevJ + dj

      if (nextI < 0 || nextI >= m || nextJ < 0 || nextJ >= n) continue
      if (grid[nextI][nextJ] !== 1) continue
      const resp = `${nextI},${nextJ}`
      if (seen.has(resp)) continue

      seen.add(`${nextI},${nextJ}`)
      queue.push([nextI, nextJ])
    }
  }

  return count
}

const DIRECTIONS = [[1, 0], [-1, 0], [0, 1], [0, -1]]
// @lc code=end
