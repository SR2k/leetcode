/*
 * @lc app=leetcode.cn id=739 lang=typescript
 *
 * [739] 每日温度
 *
 * https://leetcode-cn.com/problems/daily-temperatures/description/
 *
 * algorithms
 * Medium (68.54%)
 * Likes:    1027
 * Dislikes: 0
 * Total Accepted:    253.4K
 * Total Submissions: 369.2K
 * Testcase Example:  '[73,74,75,71,69,72,76,73]'
 *
 * 给定一个整数数组 temperatures ，表示每天的温度，返回一个数组 answer ，其中 answer[i] 是指在第 i
 * 天之后，才会有更高的温度。如果气温在这之后都不会升高，请在该位置用 0 来代替。
 *
 *
 *
 * 示例 1:
 *
 *
 * 输入: temperatures = [73,74,75,71,69,72,76,73]
 * 输出: [1,1,4,2,1,1,0,0]
 *
 *
 * 示例 2:
 *
 *
 * 输入: temperatures = [30,40,50,60]
 * 输出: [1,1,1,0]
 *
 *
 * 示例 3:
 *
 *
 * 输入: temperatures = [30,60,90]
 * 输出: [1,1,0]
 *
 *
 *
 * 提示：
 *
 *
 * 1 <= temperatures.length <= 10^5
 * 30 <= temperatures[i] <= 100
 *
 *
 */

export
// @lc code=start
function dailyTemperatures(temperatures: number[]): number[] {
  const result = temperatures.map(() => 0)
  const stack: number[] = []

  temperatures.forEach((t, i) => {
    while (stack.length && temperatures[stack[stack.length - 1]] < t) {
      const prev = stack.pop()!
      result[prev] = i - prev
    }
    stack.push(i)
  })

  return result
}
// @lc code=end
