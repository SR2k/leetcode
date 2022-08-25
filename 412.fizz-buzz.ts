/*
 * @lc app=leetcode.cn id=412 lang=typescript
 *
 * [412] Fizz Buzz
 *
 * https://leetcode.cn/problems/fizz-buzz/description/
 *
 * algorithms
 * Easy (70.41%)
 * Likes:    212
 * Dislikes: 0
 * Total Accepted:    146.4K
 * Total Submissions: 207.9K
 * Testcase Example:  '3'
 *
 * 给你一个整数 n ，找出从 1 到 n 各个整数的 Fizz Buzz 表示，并用字符串数组 answer（下标从 1
 * 开始）返回结果，其中：
 *
 *
 * answer[i] == "FizzBuzz" 如果 i 同时是 3 和 5 的倍数。
 * answer[i] == "Fizz" 如果 i 是 3 的倍数。
 * answer[i] == "Buzz" 如果 i 是 5 的倍数。
 * answer[i] == i （以字符串形式）如果上述条件全不满足。
 *
 *
 *
 *
 * 示例 1：
 *
 *
 * 输入：n = 3
 * 输出：["1","2","Fizz"]
 *
 *
 * 示例 2：
 *
 *
 * 输入：n = 5
 * 输出：["1","2","Fizz","4","Buzz"]
 *
 *
 * 示例 3：
 *
 *
 * 输入：n = 15
 *
 * 输出：["1","2","Fizz","4","Buzz","Fizz","7","8","Fizz","Buzz","11","Fizz","13","14","FizzBuzz"]
 *
 *
 *
 * 提示：
 *
 *
 * 1 <= n <= 10^4
 *
 *
 */

export
// @lc code=start
function fizzBuzz(n: number): string[] {
  return new Array(n).fill(0).map((_, i) => {
    const x = i + 1
    if (x % 15 === 0) return 'FizzBuzz'
    if (x % 5 === 0) return 'Buzz'
    if (x % 3 === 0) return 'Fizz'
    return String(x)
  })
}
// @lc code=end
