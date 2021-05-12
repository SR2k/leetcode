/*
 * @lc app=leetcode.cn id=1262 lang=javascript
 *
 * [1262] 可被三整除的最大和
 *
 * https://leetcode-cn.com/problems/greatest-sum-divisible-by-three/description/
 *
 * algorithms
 * Medium (51.96%)
 * Likes:    124
 * Dislikes: 0
 * Total Accepted:    10.5K
 * Total Submissions: 20.2K
 * Testcase Example:  '[3,6,5,1,8]'
 *
 * 给你一个整数数组 nums，请你找出并返回能被三整除的元素最大和。
 * 
 * 
 * 
 * 
 * 
 * 
 * 示例 1：
 * 
 * 输入：nums = [3,6,5,1,8]
 * 输出：18
 * 解释：选出数字 3, 6, 1 和 8，它们的和是 18（可被 3 整除的最大和）。
 * 
 * 示例 2：
 * 
 * 输入：nums = [4]
 * 输出：0
 * 解释：4 不能被 3 整除，所以无法选出数字，返回 0。
 * 
 * 
 * 示例 3：
 * 
 * 输入：nums = [1,2,3,4,4]
 * 输出：12
 * 解释：选出数字 1, 3, 4 以及 4，它们的和是 12（可被 3 整除的最大和）。
 * 
 * 
 * 
 * 
 * 提示：
 * 
 * 
 * 1 <= nums.length <= 4 * 10^4
 * 1 <= nums[i] <= 10^4
 * 
 * 
 */

// @lc code=start
/**
 * @param {number[]} nums
 * @return {number}
 */
var maxSumDivThree = function(nums) {
  const dp = []

  const normalize = (x) => {
    if (x >= 3) return x % 3
    if (x >= 0) return x
    return (x % 3 + 3) % 3
  }

  nums.forEach((n, i) => {
    dp[i] = []

    if (i === 0) {
      dp[0][0] = n % 3 === 0 ? n : -Infinity
      dp[0][1] = n % 3 === 1 ? n : -Infinity
      dp[0][2] = n % 3 === 2 ? n : -Infinity
    } else {
      const x = n % 3;
      dp[i][0] = Math.max(dp[i - 1][0], dp[i-1][(3 - x) % 3] + n);
      dp[i][1] = Math.max(dp[i - 1][1], dp[i-1][(3 - x + 1) % 3] + n);
      dp[i][2] = Math.max(dp[i - 1][2], dp[i-1][(3 - x + 2) % 3] + n);

      dp[i][normalize(x)] = Math.max(dp[i][normalize(x)], n)
    }
  })

  return dp[nums.length - 1][0] === -Infinity ? 0 : dp[nums.length - 1][0]
};
// @lc code=end

// console.log(maxSumDivThree([2,19,6,16,5,10,7,4,11,6]))

