/*
 * @lc app=leetcode.cn id=84 lang=typescript
 *
 * [84] 柱状图中最大的矩形
 *
 * https://leetcode.cn/problems/largest-rectangle-in-histogram/description/
 *
 * algorithms
 * Hard (44.32%)
 * Likes:    1981
 * Dislikes: 0
 * Total Accepted:    257.5K
 * Total Submissions: 580.8K
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
  const stack: number[] = []
  let result = 0

  heights.forEach((h, i) => {
    while (stack.length && heights[stack[stack.length - 1]] >= h) {
      const prevIndex = stack.pop()!
      result = Math.max(result, heights[prevIndex] * (i - left[prevIndex] - 1))
    }

    if (stack.length) {
      left[i] = stack[stack.length - 1]
    }
    stack.push(i)
  })

  while (stack.length) {
    const prevIndex = stack.pop()!
    result = Math.max(result, heights[prevIndex] * (heights.length - left[prevIndex] - 1))
  }

  return result
}

// function largestRectangleArea(heights: number[]): number {
//   const left = new Array(heights.length).fill(0).map((_, i) => i)
//   let stack: number[] = []
//   heights.forEach((h, i) => {
//     while (stack.length && heights[stack[stack.length - 1]] >= h) {
//       stack.pop()
//     }
//     if (!stack.length) {
//       left[i] = 0
//     } else {
//       left[i] = stack[stack.length - 1] + 1
//     }
//     stack.push(i)
//   })

//   // console.log(left)

//   const right = new Array(heights.length).fill(0).map((_, i) => i)
//   stack = []
//   for (let i = right.length - 1; i >= 0; i--) {
//     while (stack.length && heights[stack[stack.length - 1]] >= heights[i]) {
//       stack.pop()
//     }
//     if (!stack.length) {
//       right[i] = right.length - 1
//     } else {
//       right[i] = stack[stack.length - 1] - 1
//     }
//     stack.push(i)
//   }
//   // console.log(right)

//   // console.log(left, right)

//   let result = 0
//   heights.forEach((h, i) => {
//     // console.log(h, right[i] - left[i] + 1, `${h} * (${right[i]} - ${left[i]} + 1) = ${h * (right[i] - left[i] + 1)}`)
//     result = Math.max(h * (right[i] - left[i] + 1), result)
//   })

//   return result
// }
// @lc code=end
