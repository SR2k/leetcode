/*
 * @lc app=leetcode.cn id=118 lang=typescript
 *
 * [118] 杨辉三角
 *
 * https://leetcode.cn/problems/pascals-triangle/description/
 *
 * algorithms
 * Easy (75.29%)
 * Likes:    824
 * Dislikes: 0
 * Total Accepted:    337K
 * Total Submissions: 447.6K
 * Testcase Example:  '5'
 *
 * 给定一个非负整数 numRows，生成「杨辉三角」的前 numRows 行。
 *
 * 在「杨辉三角」中，每个数是它左上方和右上方的数的和。
 *
 *
 *
 *
 *
 * 示例 1:
 *
 *
 * 输入: numRows = 5
 * 输出: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
 *
 *
 * 示例 2:
 *
 *
 * 输入: numRows = 1
 * 输出: [[1]]
 *
 *
 *
 *
 * 提示:
 *
 *
 * 1
 *
 *
 */

export
// @lc code=start
const memo = (fn: (n: number) => number[][]) => {
  const memoBook = new Map<number, ReturnType<typeof fn>>()

  function memoed(n: number) {
    if (!memoBook.get(n)) {
      memoBook.set(n, fn(n))
    }

    return memoBook.get(n)!
  }

  return memoed
}

const generate = memo((numRows: number): number[][] => {
  if (numRows === 1) {
    return [[1]]
  }

  const prevResult = generate(numRows - 1)
  const prev = prevResult.at(-1)!

  const curr = [1]

  for (let i = 0; i < prev.length - 1; i++) {
    curr.push(prev[i] + prev[i + 1])
  }

  curr.push(1)
  return [...prevResult, curr]
})
// @lc code=end
