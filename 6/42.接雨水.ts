/*
 * @lc app=leetcode.cn id=42 lang=typescript
 *
 * [42] 接雨水
 *
 * https://leetcode.cn/problems/trapping-rain-water/description/
 *
 * algorithms
 * Hard (61.13%)
 * Likes:    3505
 * Dislikes: 0
 * Total Accepted:    497.2K
 * Total Submissions: 813.4K
 * Testcase Example:  '[0,1,0,2,1,0,1,3,2,1,2,1]'
 *
 * 给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。
 *
 *
 *
 * 示例 1：
 *
 *
 *
 *
 * 输入：height = [0,1,0,2,1,0,1,3,2,1,2,1]
 * 输出：6
 * 解释：上面是由数组 [0,1,0,2,1,0,1,3,2,1,2,1] 表示的高度图，在这种情况下，可以接 6 个单位的雨水（蓝色部分表示雨水）。
 *
 *
 * 示例 2：
 *
 *
 * 输入：height = [4,2,0,3,2,5]
 * 输出：9
 *
 *
 *
 *
 * 提示：
 *
 *
 * n == height.length
 * 1 <= n <= 2 * 10^4
 * 0 <= height[i] <= 10^5
 *
 *
 */

export
// @lc code=start
function trap(height: number[]): number {
  let i = 0, j = height.length - 1
  let leftMax = height[i], rightMax = height[j]
  let result = 0

  while (i <= j) {
    if (leftMax <= rightMax) {
      leftMax = Math.max(leftMax, height[i])
      result += leftMax - height[i]
      i++
    } else {
      rightMax = Math.max(rightMax, height[j])
      result += rightMax - height[j]
      j--
    }
  }

  return result
}
// @lc code=end
