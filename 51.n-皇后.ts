/*
 * @lc app=leetcode.cn id=51 lang=typescript
 *
 * [51] N 皇后
 *
 * https://leetcode.cn/problems/n-queens/description/
 *
 * algorithms
 * Hard (74.10%)
 * Likes:    1466
 * Dislikes: 0
 * Total Accepted:    243.2K
 * Total Submissions: 328.2K
 * Testcase Example:  '4'
 *
 * 按照国际象棋的规则，皇后可以攻击与之处在同一行或同一列或同一斜线上的棋子。
 *
 * n 皇后问题 研究的是如何将 n 个皇后放置在 n×n 的棋盘上，并且使皇后彼此之间不能相互攻击。
 *
 * 给你一个整数 n ，返回所有不同的 n 皇后问题 的解决方案。
 *
 *
 *
 * 每一种解法包含一个不同的 n 皇后问题 的棋子放置方案，该方案中 'Q' 和 '.' 分别代表了皇后和空位。
 *
 *
 *
 * 示例 1：
 *
 *
 * 输入：n = 4
 * 输出：[[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
 * 解释：如上图所示，4 皇后问题存在两个不同的解法。
 *
 *
 * 示例 2：
 *
 *
 * 输入：n = 1
 * 输出：[["Q"]]
 *
 *
 *
 *
 * 提示：
 *
 *
 * 1 <= n <= 9
 *
 *
 *
 *
 */

export
// @lc code=start
function solveNQueens(n: number): string[][] {
  let row = 0, col = 0, diag = 0, revr = 0

  const grid: CellTypes[][] = new Array(n).fill(0).map(() => (
    new Array(n).fill(CellTypes.Empty)
  ))
  const result: string[][] = []

  function helper(i: number, j: number, queenCount: number) {
    if (i === n) {
      if (queenCount === n) {
        result.push(grid.map((r) => r.join('')))
      }
      return
    }

    if (queenCount < i) return

    const [nextI, nextJ] = next(i, j, n)
    helper(nextI, nextJ, queenCount)

    const [d, r] = getDiag(i, j, n)
    if (row & (1 << i) || col & (1 << j) || diag & (1 << d) || revr & (1 << r)) {
      return
    }

    row ^= (1 << i)
    col ^= (1 << j)
    diag ^= (1 << d)
    revr ^= (1 << r)
    grid[i][j] = CellTypes.Queen

    helper(nextI, nextJ, queenCount + 1)

    row ^= (1 << i)
    col ^= (1 << j)
    diag ^= (1 << d)
    revr ^= (1 << r)
    grid[i][j] = CellTypes.Empty
  }

  helper(0, 0, 0)
  return result
}

const enum CellTypes {
  Queen = 'Q',
  Empty = '.',
}

const getDiag = (i: number, j: number, n: number) => [i + j, i - j + n - 1]

const next = (i: number, j: number, n: number) => {
  if (j === n - 1) return [i + 1, 0]
  return [i, j + 1]
}
// @lc code=end
