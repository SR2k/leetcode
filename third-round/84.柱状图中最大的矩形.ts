/*
 * @lc app=leetcode.cn id=84 lang=typescript
 *
 * [84] 柱状图中最大的矩形
 *
 * https://leetcode-cn.com/problems/largest-rectangle-in-histogram/description/
 *
 * algorithms
 * Hard (43.70%)
 * Likes:    1773
 * Dislikes: 0
 * Total Accepted:    216.2K
 * Total Submissions: 493.8K
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

// TODO: one pass solution
export
// @lc code=start
function largestRectangleArea(heights: number[]): number {
  const left = heights.map((x, i) => i - 1)
  const right = heights.map((x, i) => i + 1)

  let stack: number[] = []
  for (let i = 0; i < heights.length; i++) {
    const height = heights[i]
    while (stack.length && heights[stack[stack.length - 1]] >= height) {
      stack.pop()
    }
    left[i] = stack.length ? stack[stack.length - 1] : -1
    stack.push(i)
  }

  stack = []
  for (let i = heights.length - 1; i >= 0; i--) {
    const height = heights[i]
    while (stack.length && heights[stack[stack.length - 1]] >= height) {
      stack.pop()
    }
    right[i] = stack.length ? stack[stack.length - 1] : heights.length
    stack.push(i)
  }

  let result = 0
  for (let i = 0; i < heights.length; i++) {
    const w = right[i] - left[i] - 1
    const h = heights[i]
    result = Math.max(w * h, result)
  }

  return result
}
// @lc code=end
