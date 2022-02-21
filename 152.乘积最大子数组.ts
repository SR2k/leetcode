/*
 * @lc app=leetcode.cn id=152 lang=typescript
 *
 * [152] 乘积最大子数组
 *
 * https://leetcode-cn.com/problems/maximum-product-subarray/description/
 *
 * algorithms
 * Medium (42.32%)
 * Likes:    1453
 * Dislikes: 0
 * Total Accepted:    212.5K
 * Total Submissions: 502.3K
 * Testcase Example:  '[2,3,-2,4]'
 *
 * 给你一个整数数组 nums ，请你找出数组中乘积最大的连续子数组（该子数组中至少包含一个数字），并返回该子数组所对应的乘积。
 *
 *
 *
 * 示例 1:
 *
 * 输入: [2,3,-2,4]
 * 输出: 6
 * 解释: 子数组 [2,3] 有最大乘积 6。
 *
 *
 * 示例 2:
 *
 * 输入: [-2,0,-1]
 * 输出: 0
 * 解释: 结果不能为 2, 因为 [-2,-1] 不是子数组。
 *
 */

export
// @lc code=start
function maxProduct(nums: number[]): number {
  let prevMax = 1
  let prevMin = 1
  let result = -Infinity

  for (const n of nums) {
    const candidates = [n, prevMax * n, prevMin * n]
    prevMax = Math.max(...candidates)
    prevMin = Math.min(...candidates)
    result = Math.max(result, prevMax)
  }

  return result
}
// @lc code=end
