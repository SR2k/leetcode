/*
 * @lc app=leetcode.cn id=79 lang=typescript
 *
 * [79] 单词搜索
 *
 * https://leetcode-cn.com/problems/word-search/description/
 *
 * algorithms
 * Medium (46.14%)
 * Likes:    1177
 * Dislikes: 0
 * Total Accepted:    265.4K
 * Total Submissions: 575.2K
 * Testcase Example:  '[["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]\n"ABCCED"'
 *
 * 给定一个 m x n 二维字符网格 board 和一个字符串单词 word 。如果 word 存在于网格中，返回 true ；否则，返回 false
 * 。
 *
 * 单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母不允许被重复使用。
 *
 *
 *
 * 示例 1：
 *
 *
 * 输入：board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word =
 * "ABCCED"
 * 输出：true
 *
 *
 * 示例 2：
 *
 *
 * 输入：board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word =
 * "SEE"
 * 输出：true
 *
 *
 * 示例 3：
 *
 *
 * 输入：board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word =
 * "ABCB"
 * 输出：false
 *
 *
 *
 *
 * 提示：
 *
 *
 * m == board.length
 * n = board[i].length
 * 1
 * 1
 * board 和 word 仅由大小写英文字母组成
 *
 *
 *
 *
 * 进阶：你可以使用搜索剪枝的技术来优化解决方案，使其在 board 更大的情况下可以更快解决问题？
 *
 */

export
// @lc code=start
function exist(board: string[][], word: string): boolean {
  const m = board.length
  const n = board[0].length

  function search(i: number, j: number, charIndex: number): boolean {
    if (charIndex >= word.length) {
      return true
    }

    if (i < 0 || i >= m || j < 0 || j >= n) return false
    if (board[i][j] !== word[charIndex]) return false
    if (board[i][j] === '-') return false

    const directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    board[i][j] = '-'
    for (const [di, dj] of directions) {
      if (search(i + di, j + dj, charIndex + 1)) {
        return true
      }
    }
    board[i][j] = word[charIndex]
    return false
  }

  for (let i = 0; i < m; i++) {
    for (let j = 0; j < n; j++) {
      if (search(i, j, 0)) {
        return true
      }
    }
  }

  return false
}
// @lc code=end
