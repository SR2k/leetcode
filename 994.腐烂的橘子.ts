/*
 * @lc app=leetcode.cn id=994 lang=typescript
 *
 * [994] 腐烂的橘子
 *
 * https://leetcode-cn.com/problems/rotting-oranges/description/
 *
 * algorithms
 * Medium (50.74%)
 * Likes:    360
 * Dislikes: 0
 * Total Accepted:    41.7K
 * Total Submissions: 82.1K
 * Testcase Example:  '[[2,1,1],[1,1,0],[0,1,1]]'
 *
 * 在给定的网格中，每个单元格可以有以下三个值之一：
 * 
 * 
 * 值 0 代表空单元格；
 * 值 1 代表新鲜橘子；
 * 值 2 代表腐烂的橘子。
 * 
 * 
 * 每分钟，任何与腐烂的橘子（在 4 个正方向上）相邻的新鲜橘子都会腐烂。
 * 
 * 返回直到单元格中没有新鲜橘子为止所必须经过的最小分钟数。如果不可能，返回 -1。
 * 
 * 
 * 
 * 示例 1：
 * 
 * 
 * 
 * 输入：[[2,1,1],[1,1,0],[0,1,1]]
 * 输出：4
 * 
 * 
 * 示例 2：
 * 
 * 输入：[[2,1,1],[0,1,1],[1,0,1]]
 * 输出：-1
 * 解释：左下角的橘子（第 2 行， 第 0 列）永远不会腐烂，因为腐烂只会发生在 4 个正向上。
 * 
 * 
 * 示例 3：
 * 
 * 输入：[[0,2]]
 * 输出：0
 * 解释：因为 0 分钟时已经没有新鲜橘子了，所以答案就是 0 。
 * 
 * 
 * 
 * 
 * 提示：
 * 
 * 
 * 1 <= grid.length <= 10
 * 1 <= grid[0].length <= 10
 * grid[i][j] 仅为 0、1 或 2
 * 
 * 
 */

// @lc code=start
function orangesRotting(grid: number[][]): number {
  const queue: [number, number][] = []
  let orangeCount = 0
  for (let i = 0; i < grid.length; i++) {
    for (let j = 0; j < grid[0].length; j++) {
      if (grid[i][j] === 1) {
        orangeCount++
      } else if (grid[i][j] === 2) {
        queue.push([i, j])
        orangeCount++
      }
    }
  }

  if (!orangeCount) return 0

  let levelCount = -1
  while (queue.length) {
    let levelSize = queue.length
    levelCount++

    while (levelSize) {
      const orange = queue.shift()
      const [i, j] = orange
      orangeCount-
      levelSize--

      if (grid[i - 1]?.[j] === 1) {
        grid[i - 1][j] = 2
        queue.push([i - 1, j])
      }
      if (grid[i + 1]?.[j] === 1) {
        grid[i + 1][j] = 2
        queue.push([i + 1, j])
      }
      if (grid[i]?.[j - 1] === 1) {
        grid[i][j - 1] = 2
        queue.push([i, j - 1])
      }
      if (grid[i]?.[j + 1] === 1) {
        grid[i][j + 1] = 2
        queue.push([i, j + 1])
      }
    }
  }

  if (orangeCount) return -1
  return levelCount
};
// @lc code=end

