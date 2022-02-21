/*
 * @lc app=leetcode.cn id=37 lang=typescript
 *
 * [37] 解数独
 *
 * https://leetcode-cn.com/problems/sudoku-solver/description/
 *
 * algorithms
 * Hard (67.08%)
 * Likes:    1095
 * Dislikes: 0
 * Total Accepted:    116.8K
 * Total Submissions: 174.1K
 * Testcase Example:  '[["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]'
 *
 * 编写一个程序，通过填充空格来解决数独问题。
 *
 * 数独的解法需 遵循如下规则：
 *
 *
 * 数字 1-9 在每一行只能出现一次。
 * 数字 1-9 在每一列只能出现一次。
 * 数字 1-9 在每一个以粗实线分隔的 3x3 宫内只能出现一次。（请参考示例图）
 *
 *
 * 数独部分空格内已填入了数字，空白格用 '.' 表示。
 *
 *
 *
 *
 *
 *
 * 示例：
 *
 *
 * 输入：board =
 * [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
 *
 * 输出：[["5","3","4","6","7","8","9","1","2"],["6","7","2","1","9","5","3","4","8"],["1","9","8","3","4","2","5","6","7"],["8","5","9","7","6","1","4","2","3"],["4","2","6","8","5","3","7","9","1"],["7","1","3","9","2","4","8","5","6"],["9","6","1","5","3","7","2","8","4"],["2","8","7","4","1","9","6","3","5"],["3","4","5","2","8","6","1","7","9"]]
 * 解释：输入的数独如上图所示，唯一有效的解决方案如下所示：
 *
 *
 *
 *
 *
 *
 * 提示：
 *
 *
 * board.length == 9
 * board[i].length == 9
 * board[i][j] 是一位数字或者 '.'
 * 题目数据 保证 输入数独仅有一个解
 *
 *
 *
 *
 *
 */

export
// @lc code=start
function solveSudoku(board: string[][]): void {
  const rows = new Array(9).fill(0).map(() => new Set<string>())
  const cols = new Array(9).fill(0).map(() => new Set<string>())
  const zones = new Array(9).fill(0).map(() => new Set<string>())

  board.forEach((row, i) => {
    row.forEach((cell, j) => {
      if (cell === '.') return
      rows[i].add(cell)
      cols[j].add(cell)
      zones[ij2z(i, j)].add(cell)
    })
  })

  function helper(i: number, j: number): boolean {
    if (i === 9) {
      return true
    }

    const [nextI, nextJ] = getNext(i, j)
    if (board[i][j] !== '.') {
      return helper(nextI, nextJ)
    }

    const k = ij2z(i, j)
    const options = getAvaliable(rows[i], cols[j], zones[k])
    if (!options.size) return false

    for (const option of options) {
      board[i][j] = option
      rows[i].add(option)
      cols[j].add(option)
      zones[k].add(option)

      if (helper(nextI, nextJ)) {
        return true
      }

      rows[i].delete(option)
      cols[j].delete(option)
      zones[k].delete(option)
      board[i][j] = '.'
    }
    return false
  }

  helper(0, 0)
}

function ij2z(i: number, j: number): number {
  return Math.floor(i / 3) * 3 + Math.floor(j / 3)
}

const allAvaliable = new Array(9).fill(0).map((n, i) => String(i + 1))
function getAvaliable(row: Set<string>, col: Set<string>, zone: Set<string>) {
  const avaliable = new Set(allAvaliable)
  for (const c of row) avaliable.delete(c)
  for (const c of col) avaliable.delete(c)
  for (const c of zone) avaliable.delete(c)

  return avaliable
}

function getNext(i: number, j: number) {
  if (j === 8) {
    return [i + 1, 0]
  }
  return [i, j + 1]
}
// @lc code=end
