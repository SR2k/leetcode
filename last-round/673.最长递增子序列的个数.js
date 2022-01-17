/*
 * @lc app=leetcode.cn id=673 lang=javascript
 *
 * [673] 最长递增子序列的个数
 *
 * https://leetcode-cn.com/problems/number-of-longest-increasing-subsequence/description/
 *
 * algorithms
 * Medium (37.82%)
 * Likes:    303
 * Dislikes: 0
 * Total Accepted:    21.4K
 * Total Submissions: 56.6K
 * Testcase Example:  '[1,3,5,4,7]'
 *
 * 给定一个未排序的整数数组，找到最长递增子序列的个数。
 * 
 * 示例 1:
 * 
 * 
 * 输入: [1,3,5,4,7]
 * 输出: 2
 * 解释: 有两个最长递增子序列，分别是 [1, 3, 4, 7] 和[1, 3, 5, 7]。
 * 
 * 
 * 示例 2:
 * 
 * 
 * 输入: [2,2,2,2,2]
 * 输出: 5
 * 解释: 最长递增子序列的长度是1，并且存在5个子序列的长度为1，因此输出5。
 * 
 * 
 * 注意: 给定的数组长度不超过 2000 并且结果一定是32位有符号整数。
 * 
 */

// @lc code=start
/**
 * @param {number[]} nums
 * @return {number}
 */
var findNumberOfLIS = function(nums) {
  let max = 0
  const dp = [0]
  for (let i = 1; i <= nums.length; i++) {
    dp[i] = nums[i] > nums[i - 1] ? dp[i - 1] + 1 : 1
    max = Math.max(max, dp[i])
  }

  let count = 0
  for (const k of dp) if (k === max) count++

  return count
};
// @lc code=end

