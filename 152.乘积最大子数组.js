/*
 * @lc app=leetcode.cn id=152 lang=javascript
 *
 * [152] 乘积最大子数组
 *
 * https://leetcode-cn.com/problems/maximum-product-subarray/description/
 *
 * algorithms
 * Medium (41.44%)
 * Likes:    1084
 * Dislikes: 0
 * Total Accepted:    139K
 * Total Submissions: 335.5K
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

// @lc code=start
/**
 * @param {number[]} nums
 * @return {number}
 */
var maxProduct = function(nums) {
  // f(i) 表示恰好以下标为 i 的元素为最后一个元素的子数组中，乘积最大的
  let maxPrev = nums[0]
  let minPrev = nums[0]
  let max = maxPrev

  for (let i = 1; i < nums.length; i++) {
    let innerMaxPrev = maxPrev
    let innerMinPrev = minPrev
    maxPrev = Math.max(innerMaxPrev * nums[i], innerMinPrev * nums[i], nums[i])
    minPrev = Math.min(innerMaxPrev * nums[i], innerMinPrev * nums[i], nums[i])

    max = Math.max(maxPrev, max)
  }

  return max
};
// @lc code=end

// console.log(maxProduct([-4,-3,-2]))
