/*
 * @lc app=leetcode.cn id=348 lang=typescript
 *
 * [348] 设计井字棋
 *
 * https://leetcode-cn.com/problems/design-tic-tac-toe/description/
 *
 * algorithms
 * Medium (60.25%)
 * Likes:    101
 * Dislikes: 0
 * Total Accepted:    5.8K
 * Total Submissions: 9.6K
 * Testcase Example:  '["TicTacToe","move","move","move","move","move","move","move"]\n' +
  '[[3],[0,0,1],[0,2,2],[2,2,1],[1,1,2],[2,0,1],[1,0,2],[2,1,1]]'
 *
 * 请在 n × n 的棋盘上，实现一个判定井字棋（Tic-Tac-Toe）胜负的神器，判断每一次玩家落子后，是否有胜出的玩家。
 *
 * 在这个井字棋游戏中，会有 2 名玩家，他们将轮流在棋盘上放置自己的棋子。
 *
 * 在实现这个判定器的过程中，你可以假设以下这些规则一定成立：
 *
 * 1. 每一步棋都是在棋盘内的，并且只能被放置在一个空的格子里；
 *
 * 2. 一旦游戏中有一名玩家胜出的话，游戏将不能再继续；
 *
 * 3. 一个玩家如果在同一行、同一列或者同一斜对角线上都放置了自己的棋子，那么他便获得胜利。
 *
 * 示例:
 *
 * 给定棋盘边长 n = 3, 玩家 1 的棋子符号是 "X"，玩家 2 的棋子符号是 "O"。
 *
 * TicTacToe toe = new TicTacToe(3);
 *
 * toe.move(0, 0, 1); -> 函数返回 0 (此时，暂时没有玩家赢得这场对决)
 * |X| | |
 * | | | |    // 玩家 1 在 (0, 0) 落子。
 * | | | |
 *
 * toe.move(0, 2, 2); -> 函数返回 0 (暂时没有玩家赢得本场比赛)
 * |X| |O|
 * | | | |    // 玩家 2 在 (0, 2) 落子。
 * | | | |
 *
 * toe.move(2, 2, 1); -> 函数返回 0 (暂时没有玩家赢得比赛)
 * |X| |O|
 * | | | |    // 玩家 1 在 (2, 2) 落子。
 * | | |X|
 *
 * toe.move(1, 1, 2); -> 函数返回 0 (暂没有玩家赢得比赛)
 * |X| |O|
 * | |O| |    // 玩家 2 在 (1, 1) 落子。
 * | | |X|
 *
 * toe.move(2, 0, 1); -> 函数返回 0 (暂无玩家赢得比赛)
 * |X| |O|
 * | |O| |    // 玩家 1 在 (2, 0) 落子。
 * |X| |X|
 *
 * toe.move(1, 0, 2); -> 函数返回 0 (没有玩家赢得比赛)
 * |X| |O|
 * |O|O| |    // 玩家 2 在 (1, 0) 落子.
 * |X| |X|
 *
 * toe.move(2, 1, 1); -> 函数返回 1 (此时，玩家 1 赢得了该场比赛)
 * |X| |O|
 * |O|O| |    // 玩家 1 在 (2, 1) 落子。
 * |X|X|X|
 *
 *
 *
 *
 * 进阶:
 * 您有没有可能将每一步的 move() 操作优化到比 O(n^2) 更快吗?
 *
 */

export
// @lc code=start
class TicTacToe {
  private readonly rows: number[]

  private readonly cols: number[]

  private diagonal = 0

  private reversedDiagonal = 0

  constructor(private readonly n: number) {
    this.rows = new Array(n).fill(0)
    this.cols = new Array(n).fill(0)
  }

  move(row: number, col: number, player: number): number {
    const resp = TicTacToe.getRespOfPlayer(player)

    this.rows[row] += resp
    if (this.rows[row] === this.n * resp) return player

    this.cols[col] += resp
    if (this.cols[col] === this.n * resp) return player

    if (row === col) {
      this.diagonal += resp
      if (this.diagonal === this.n * resp) return player
    }

    if (row === this.n - col - 1) {
      this.reversedDiagonal += resp
      if (this.reversedDiagonal === this.n * resp) return player
    }

    return 0
  }

  private static getRespOfPlayer(player: number) {
    if (player === 1) return 1
    return -1
  }
}
// @lc code=end
