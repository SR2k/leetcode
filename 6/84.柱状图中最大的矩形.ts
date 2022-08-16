/*
 * @lc app=leetcode.cn id=84 lang=typescript
 *
 * [84] 柱状图中最大的矩形
 *
 * https://leetcode.cn/problems/largest-rectangle-in-histogram/description/
 *
 * algorithms
 * Hard (44.34%)
 * Likes:    2011
 * Dislikes: 0
 * Total Accepted:    262.4K
 * Total Submissions: 591.8K
 * Testcase Example:  '[2,1,5,6,2,3]'
 *
 * 给定 n 个非负整数，用来表示柱状图中各个柱子的高度。每个柱子彼此相邻，且宽度为 1 。
 *
 * 求在该柱状图中，能够勾勒出来的矩形的最大面积。
 *
 *
 *
 * 示例 1:
 *
 *
 *
 *
 * 输入：heights = [2,1,5,6,2,3]
 * 输出：10
 * 解释：最大的矩形为图中红色区域，面积为 10
 *
 *
 * 示例 2：
 *
 *
 *
 *
 * 输入： heights = [2,4]
 * 输出： 4
 *
 *
 *
 * 提示：
 *
 *
 * 1
 * 0
 *
 *
 */

export
// @lc code=start
function largestRectangleArea(heights: number[]): number {
  const left = heights.map(() => 0)
  const leftStack: number[] = [-1]
  for (let i = 0; i < heights.length; i++) {
    while (true) {
      const last = leftStack[leftStack.length - 1]
      if (last < 0) {
        break
      }
      if (heights[last] < heights[i]) {
        break
      }
      leftStack.pop()
    }
    left[i] = leftStack[leftStack.length - 1] + 1
    leftStack.push(i)
  }

  const rightStack: number[] = [heights.length]
  let result = 0
  for (let i = heights.length - 1; i >= 0; i--) {
    while (true) {
      const last = rightStack[rightStack.length - 1]
      if (last === heights.length) {
        break
      }
      if (heights[last] < heights[i]) {
        break
      }
      rightStack.pop()
    }
    const right = rightStack[rightStack.length - 1] - 1
    result = Math.max(result, (right - left[i] + 1) * heights[i])

    rightStack.push(i)
  }

  return result
}
// @lc code=end
