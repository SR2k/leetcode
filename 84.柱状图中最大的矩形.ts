/*
 * @lc app=leetcode.cn id=84 lang=typescript
 *
 * [84] 柱状图中最大的矩形
 *
 * https://leetcode.cn/problems/largest-rectangle-in-histogram/description/
 *
 * algorithms
 * Hard (44.59%)
 * Likes:    2127
 * Dislikes: 0
 * Total Accepted:    282.8K
 * Total Submissions: 634.3K
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
  const left = heights.map(() => -1)
  const right = heights.map(() => heights.length)
  const stack: number[] = []

  for (let i = 0; i < heights.length; i++) {
    while (stack.length && heights[stack.at(-1)!] >= heights[i]) {
      right[stack.pop()!] = i
    }
    left[i] = stack.at(-1) ?? -1
    stack.push(i)
  }

  return Math.max(
    ...heights.map((h, i) => ((right[i] - 1) - (left[i] + 1) + 1) * h),
  )
}
// @lc code=end
