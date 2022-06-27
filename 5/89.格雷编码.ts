/*
 * @lc app=leetcode.cn id=89 lang=typescript
 *
 * [89] 格雷编码
 *
 * https://leetcode.cn/problems/gray-code/description/
 *
 * algorithms
 * Medium (74.61%)
 * Likes:    501
 * Dislikes: 0
 * Total Accepted:    95.8K
 * Total Submissions: 128.2K
 * Testcase Example:  '2'
 *
 * n 位格雷码序列 是一个由 2^n 个整数组成的序列，其中：
 *
 * 每个整数都在范围 [0, 2^n - 1] 内（含 0 和 2^n - 1）
 * 第一个整数是 0
 * 一个整数在序列中出现 不超过一次
 * 每对 相邻 整数的二进制表示 恰好一位不同 ，且
 * 第一个 和 最后一个 整数的二进制表示 恰好一位不同
 *
 *
 * 给你一个整数 n ，返回任一有效的 n 位格雷码序列 。
 *
 *
 *
 * 示例 1：
 *
 *
 * 输入：n = 2
 * 输出：[0,1,3,2]
 * 解释：
 * [0,1,3,2] 的二进制表示是 [00,01,11,10] 。
 * - 00 和 01 有一位不同
 * - 01 和 11 有一位不同
 * - 11 和 10 有一位不同
 * - 10 和 00 有一位不同
 * [0,2,3,1] 也是一个有效的格雷码序列，其二进制表示是 [00,10,11,01] 。
 * - 00 和 10 有一位不同
 * - 10 和 11 有一位不同
 * - 11 和 01 有一位不同
 * - 01 和 00 有一位不同
 *
 *
 * 示例 2：
 *
 *
 * 输入：n = 1
 * 输出：[0,1]
 *
 *
 *
 *
 * 提示：
 *
 *
 * 1 <= n <= 16
 *
 *
 */

// @lc code=start
const cache: Record<number, number[]> = {}

type GrayCodeFn = (n: number) => number[]

const cached = (fn: GrayCodeFn): GrayCodeFn => (n: number) => {
  if (!cache[n]) {
    cache[n] = fn(n)
  }
  return cache[n]
}

const grayCode = cached((n) => {
  if (n === 1) {
    return [0, 1]
  }

  const result = [...grayCode(n - 1)]
  const length = result.length
  // eslint-disable-next-line for-direction
  for (let i = length - 1; i >= 0; i--) {
    result.push(result[i] | (1 << (n - 1)))
  }

  return result
})
// @lc code=end

console.log(grayCode(1))
console.log(grayCode(2))
console.log(grayCode(3))
console.log(grayCode(4))
console.log(grayCode(5))
console.log(grayCode(6))

console.log('done!')
