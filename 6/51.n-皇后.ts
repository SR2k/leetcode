/*
 * @lc app=leetcode.cn id=51 lang=typescript
 *
 * [51] N 皇后
 *
 * https://leetcode.cn/problems/n-queens/description/
 *
 * algorithms
 * Hard (74.02%)
 * Likes:    1393
 * Dislikes: 0
 * Total Accepted:    228.3K
 * Total Submissions: 308.3K
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
  let rows = 0, cols = 0, forward = 0, slash = 0

  const result: string[][] = []
  const grid: boolean[][] = new Array(n).fill(0).map(
    () => new Array(n).fill(false),
  )

  function put(i: number, j: number, queenCount = 0) {
    if (i === n) {
      if (queenCount === n) {
        result.push(
          grid.map(
            (row) => {
              const rowStringArr = row.map((cell) => (cell ? 'Q' : '.'))
              return rowStringArr.join('')
            },
          ),
        )
      }
      return
    }

    // there should be at least 1 queen each row
    if (queenCount < i) {
      return
    }

    const [ni, nj] = nextMove(i, j, n)
    put(ni, nj, queenCount)

    const r = (1 << i), c = (1 << j), f = (1 << (i + j)), s = (1 << (i - j + n - 1))
    if ((r & rows) || (c & cols) || (f & forward) || (s & slash)) {
      return
    }

    rows ^= r
    cols ^= c
    forward ^= f
    slash ^= s
    grid[i][j] = true

    put(ni, nj, queenCount + 1)

    rows ^= r
    cols ^= c
    forward ^= f
    slash ^= s
    grid[i][j] = false
  }

  put(0, 0)
  return result
}

const nextMove = (i: number, j: number, n: number): [number, number] => {
  if (j === n - 1) return [i + 1, 0]
  return [i, j + 1]
}
// @lc code=end
