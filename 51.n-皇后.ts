/*
 * @lc app=leetcode.cn id=51 lang=typescript
 *
 * [51] N 皇后
 *
 * https://leetcode-cn.com/problems/n-queens/description/
 *
 * algorithms
 * Hard (73.82%)
 * Likes:    1156
 * Dislikes: 0
 * Total Accepted:    176.1K
 * Total Submissions: 238.6K
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

export
// @lc code=start
function solveNQueens(n: number): string[][] {
  const curr = new Array(n).fill(0).map(() => new Array(n).fill(false))

  const rows = new Array(n).fill(false)
  const cols = new Array(n).fill(false)
  const diagonals = new Array(2 * n - 1).fill(false)
  const reverseDiagonals = new Array(2 * n - 1).fill(false)

  const result: string[][] = []

  function helper(i: number, j: number, queenCount: number) {
    if (i === n) {
      if (queenCount === n) {
        result.push(curr.map((row) => row.map((cell) => (cell ? 'Q' : '.')).join('')))
      }
      return
    }

    const [nextI, nextJ] = getNextIJ(i, j, n)
    helper(nextI, nextJ, queenCount)

    const d = getDiagonalIndex(i, j, n), rd = getReversedDiagonalIndex(i, j, n)
    if (rows[i] || cols[j] || diagonals[d] || reverseDiagonals[rd]) return

    curr[i][j] = true
    rows[i] = true
    cols[j] = true
    diagonals[d] = true
    reverseDiagonals[rd] = true

    helper(nextI, nextJ, queenCount + 1)

    curr[i][j] = false
    rows[i] = false
    cols[j] = false
    diagonals[d] = false
    reverseDiagonals[rd] = false
  }
  helper(0, 0, 0)

  return result
}

function getDiagonalIndex(i: number, j: number, n: number) {
  if (i >= j) {
    const row = i - j
    return n - 1 - row
  }

  const col = j - i
  return n - 1 + col
}

function getReversedDiagonalIndex(i: number, j: number, n: number) {
  const dj = n - 1 - j
  return getDiagonalIndex(i, dj, n)
}

function getNextIJ(i: number, j: number, n: number) {
  if (j === n - 1) {
    return [i + 1, 0]
  }
  return [i, j + 1]
}
// @lc code=end
