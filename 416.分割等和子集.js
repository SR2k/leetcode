/*
 * @lc app=leetcode.cn id=416 lang=javascript
 *
 * [416] 分割等和子集
 *
 * https://leetcode-cn.com/problems/partition-equal-subset-sum/description/
 *
 * algorithms
 * Medium (49.81%)
 * Likes:    777
 * Dislikes: 0
 * Total Accepted:    124.5K
 * Total Submissions: 249.9K
 * Testcase Example:  '[1,5,11,5]'
 *
 * 给你一个 只包含正整数 的 非空 数组 nums 。请你判断是否可以将这个数组分割成两个子集，使得两个子集的元素和相等。
 * 
 * 
 * 
 * 示例 1：
 * 
 * 
 * 输入：nums = [1,5,11,5]
 * 输出：true
 * 解释：数组可以分割成 [1, 5, 5] 和 [11] 。
 * 
 * 示例 2：
 * 
 * 
 * 输入：nums = [1,2,3,5]
 * 输出：false
 * 解释：数组不能分割成两个元素和相等的子集。
 * 
 * 
 * 
 * 
 * 提示：
 * 
 * 
 * 1 
 * 1 
 * 
 * 
 */

// @lc code=start
/**
 * @param {number[]} nums
 * @return {boolean}
 */
var canPartition = function(nums) {
  if (nums.length === 1) return false
  let sum = 0
  for (const n of nums) sum += n
  if (sum % 2 !== 0) return false

  const packSize = sum / 2

  const dp = [];

  for (let i = 0; i < nums.length; i++) {
    dp[i] = [];

    for (let j = 0; j <= packSize; j++) {
      if (i === 0) {
        // 第一个物品
        dp[i][j] = nums[i] === j
      } else {
        dp[i][j] = dp[i - 1][j] || dp[i - 1][j - nums[i]]
      }
    }
  }

  return dp[nums.length - 1][packSize] || false
};
// @lc code=end

