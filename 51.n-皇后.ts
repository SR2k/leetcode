/*
 * @lc app=leetcode.cn id=51 lang=typescript
 *
 * [51] N 皇后
 *
 * https://leetcode.cn/problems/n-queens/description/
 *
 * algorithms
 * Hard (74.04%)
 * Likes:    1352
 * Dislikes: 0
 * Total Accepted:    217.4K
 * Total Submissions: 293.8K
 * Testcase Example:  '4'
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

// @lc code=start
const getDiagonalResp = (i: number, j: number) => i + j
const getReverseResp = (i: number, j: number, n: number) => i - j + n

function solveNQueens(n: number): string[][] {
  const current = new Array(n).fill(0).map(() => new Array<boolean>(n).fill(false))
  const result: string[][] = []

  let rows = 0, cols = 0, diagonal = 0, reverse = 0

  const walk = (i: number, j: number, queenCount: number) => {
    if (i === n) {
      if (queenCount === n) {
        result.push(current.map((row) => row.map((cell) => (cell ? 'Q' : '.')).join('')))
      }
      return
    }

    const nextI = j === n - 1 ? i + 1 : i
    const nextJ = j === n - 1 ? 0 : j + 1

    const x = getDiagonalResp(i, j), y = getReverseResp(i, j, n)
    if (!((rows & (1 << i)) || (cols & (1 << j)) || (diagonal & (1 << x)) || (reverse & (1 << y)))) {
      rows ^= 1 << i
      cols ^= 1 << j
      diagonal ^= 1 << x
      reverse ^= 1 << y
      current[i][j] = true

      walk(nextI, nextJ, queenCount + 1)

      rows ^= 1 << i
      cols ^= 1 << j
      diagonal ^= 1 << x
      reverse ^= 1 << y
      current[i][j] = false
    }

    walk(nextI, nextJ, queenCount)
  }

  walk(0, 0, 0)
  return result
}
// @lc code=end
