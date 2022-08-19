/*
 * @lc app=leetcode.cn id=152 lang=typescript
 *
 * [152] 乘积最大子数组
 *
 * https://leetcode.cn/problems/maximum-product-subarray/description/
 *
 * algorithms
 * Medium (42.93%)
 * Likes:    1756
 * Dislikes: 0
 * Total Accepted:    299.1K
 * Total Submissions: 696.4K
 * Testcase Example:  '[2,3,-2,4]'
 *
 * 给你一个整数数组 nums ，请你找出数组中乘积最大的非空连续子数组（该子数组中至少包含一个数字），并返回该子数组所对应的乘积。
 *
 * 测试用例的答案是一个 32-位 整数。
 *
 * 子数组 是数组的连续子序列。
 *
 *
 *
 * 示例 1:
 *
 *
 * 输入: nums = [2,3,-2,4]
 * 输出: 6
 * 解释: 子数组 [2,3] 有最大乘积 6。
 *
 *
 * 示例 2:
 *
 *
 * 输入: nums = [-2,0,-1]
 * 输出: 0
 * 解释: 结果不能为 2, 因为 [-2,-1] 不是子数组。
 *
 *
 *
 * 提示:
 *
 *
 * 1 <= nums.length <= 2 * 10^4
 * -10 <= nums[i] <= 10
 * nums 的任何前缀或后缀的乘积都 保证 是一个 32-位 整数
 *
 *
 */

export
// @lc code=start
function maxProduct(nums: number[]): number {
  let max = 1, min = 1
  let result = nums[0]
  let hasZero = false

  for (let i = 0; i < nums.length; i++) {
    const n = nums[i]

    if (n === 0) {
      hasZero = true
      max = 1
      min = 1
    } else {
      [max, min] = [
        Math.max(n, n * max, n * min),
        Math.min(n, n * max, n * min),
      ]
      result = Math.max(max, result)
    }
  }

  return hasZero
    ? Math.max(result, 0)
    : result
}
// @lc code=end
