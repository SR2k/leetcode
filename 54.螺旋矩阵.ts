/*
 * @lc app=leetcode.cn id=54 lang=typescript
 *
 * [54] 螺旋矩阵
 *
 * https://leetcode-cn.com/problems/spiral-matrix/description/
 *
 * algorithms
 * Medium (48.34%)
 * Likes:    963
 * Dislikes: 0
 * Total Accepted:    214.4K
 * Total Submissions: 443.5K
 * Testcase Example:  '[[1,2,3],[4,5,6],[7,8,9]]'
 *
 * 给你一个 m 行 n 列的矩阵 matrix ，请按照 顺时针螺旋顺序 ，返回矩阵中的所有元素。
 *
 *
 *
 * 示例 1：
 *
 *
 * 输入：matrix = [[1,2,3],[4,5,6],[7,8,9]]
 * 输出：[1,2,3,6,9,8,7,4,5]
 *
 *
 * 示例 2：
 *
 *
 * 输入：matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
 * 输出：[1,2,3,4,8,12,11,10,9,5,6,7]
 *
 *
 *
 *
 * 提示：
 *
 *
 * m == matrix.length
 * n == matrix[i].length
 * 1
 * -100
 *
 *
 */

export
// @lc code=start
function spiralOrder(matrix: number[][]): number[] {
  const m = matrix.length; const
    n = matrix[0].length
  const DIRECTIONS: Array<[number, number]> = [[0, 1], [1, 0], [0, -1], [-1, 0]]
  const edges = [n - 1, m - 1, 0, 0]
  let direction = Directions.Right
  const result = []

  let i = 0; let
    j = -1
  while (result.length < m * n) {
    switch (direction) {
      case Directions.Right: {
        if (edges[direction] === j) {
          edges[Directions.Up] += 1
          direction = Directions.Down
        }
        break
      }
      case Directions.Down: {
        if (edges[direction] === i) {
          edges[Directions.Right] -= 1
          direction = Directions.Left
        }
        break
      }
      case Directions.Left:
        if (edges[direction] === j) {
          edges[Directions.Down] -= 1
          direction = Directions.Up
        }
        break
      case Directions.Up: {
        if (edges[direction] === i) {
          edges[Directions.Left] += 1
          direction = Directions.Right
        }
      }
    }

    i += DIRECTIONS[direction][0]
    j += DIRECTIONS[direction][1]
    result.push(matrix[i][j])
  }

  return result
}

const enum Directions {
  Right,
  Down,
  Left,
  Up,
}
// @lc code=end
