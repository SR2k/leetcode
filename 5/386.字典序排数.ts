/*
 * @lc app=leetcode.cn id=386 lang=typescript
 *
 * [386] 字典序排数
 *
 * https://leetcode.cn/problems/lexicographical-numbers/description/
 *
 * algorithms
 * Medium (75.13%)
 * Likes:    395
 * Dislikes: 0
 * Total Accepted:    62.1K
 * Total Submissions: 82.7K
 * Testcase Example:  '13'
 *
 * 给你一个整数 n ，按字典序返回范围 [1, n] 内所有整数。
 *
 * 你必须设计一个时间复杂度为 O(n) 且使用 O(1) 额外空间的算法。
 *
 *
 *
 * 示例 1：
 *
 *
 * 输入：n = 13
 * 输出：[1,10,11,12,13,2,3,4,5,6,7,8,9]
 *
 *
 * 示例 2：
 *
 *
 * 输入：n = 2
 * 输出：[1,2]
 *
 *
 *
 *
 * 提示：
 *
 *
 * 1 <= n <= 5 * 10^4
 *
 *
 */

export
// @lc code=start
function lexicalOrder(n: number): number[] {
  let curr = 1
  const result: number[] = []

  while (result.length < n) {
    while (curr <= n) {
      result.push(curr)
      curr *= 10
    }

    while (curr % 10 === 9 || curr > n) {
      curr = Math.floor(curr / 10)
    }

    curr += 1
  }

  return result
}
// @lc code=end
