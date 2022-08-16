/*
 * @lc app=leetcode.cn id=52 lang=typescript
 *
 * [52] N皇后 II
 *
 * https://leetcode.cn/problems/n-queens-ii/description/
 *
 * algorithms
 * Hard (82.25%)
 * Likes:    374
 * Dislikes: 0
 * Total Accepted:    96.3K
 * Total Submissions: 117.1K
 * Testcase Example:  '4'
 *
 * n 皇后问题 研究的是如何将 n 个皇后放置在 n × n 的棋盘上，并且使皇后彼此之间不能相互攻击。
 *
 * 给你一个整数 n ，返回 n 皇后问题 不同的解决方案的数量。
 *
 *
 *
 *
 *
 * 示例 1：
 *
 *
 * 输入：n = 4
 * 输出：2
 * 解释：如上图所示，4 皇后问题存在两个不同的解法。
 *
 *
 * 示例 2：
 *
 *
 * 输入：n = 1
 * 输出：1
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
function totalNQueens(n: number): number {
  let rows = 0; let cols = 0; let diagonals = 0; let reverse = 0
  let result = 0

  function helper(i: number, j: number, queenCount: number) {
    if (i === n) {
      if (queenCount === n) {
        result++
      }
      return
    }

    const [ni, nj] = next(i, j, n)
    helper(ni, nj, queenCount)

    const ro = (1 << i), c = (1 << j), d = (1 << (i + j)), r = (1 << i - j + n - 1)
    if ((rows & ro) || (cols & c) || (diagonals & d) || (reverse & r)) {
      return
    }

    rows ^= ro
    cols ^= c
    diagonals ^= d
    reverse ^= r

    helper(ni, nj, queenCount + 1)

    rows ^= ro
    cols ^= c
    diagonals ^= d
    reverse ^= r
  }

  helper(0, 0, 0)
  return result
}

const next = (i: number, j: number, n: number): [number, number] => {
  if (j === n - 1) {
    return [i + 1, 0]
  }
  return [i, j + 1]
}
// @lc code=end
