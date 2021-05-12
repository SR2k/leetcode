/*
 * @lc app=leetcode.cn id=523 lang=javascript
 *
 * [523] 连续的子数组和
 *
 * https://leetcode-cn.com/problems/continuous-subarray-sum/description/
 *
 * algorithms
 * Medium (22.76%)
 * Likes:    226
 * Dislikes: 0
 * Total Accepted:    30.4K
 * Total Submissions: 133.4K
 * Testcase Example:  '[23,2,4,6,7]\n6'
 *
 * 给定一个包含 非负数 的数组和一个目标 整数 k ，编写一个函数来判断该数组是否含有连续的子数组，其大小至少为 2，且总和为 k 的倍数，即总和为 n
 * * k ，其中 n 也是一个整数。
 * 
 * 
 * 
 * 示例 1：
 * 
 * 
 * 输入：[23,2,4,6,7], k = 6
 * 输出：True
 * 解释：[2,4] 是一个大小为 2 的子数组，并且和为 6。
 * 
 * 
 * 示例 2：
 * 
 * 
 * 输入：[23,2,6,4,7], k = 6
 * 输出：True
 * 解释：[23,2,6,4,7]是大小为 5 的子数组，并且和为 42。
 * 
 * 
 * 
 * 
 * 说明：
 * 
 * 
 * 数组的长度不会超过 10,000 。
 * 你可以认为所有数字总和在 32 位有符号整数范围内。
 * 
 * 
 */

// @lc code=start
/**
 * @param {number[]} nums
 * @param {number} k
 * @return {boolean}
 */
var checkSubarraySum = function(nums, k) {
  if (!nums || nums.length <= 1) return false

  const normalize = (x) => {
    if (x >= k) return x % k
    return (x % k + k) % k
  }

  let prev = []

  for (let i = 0; i < nums.length; i++) {
    const curr = []

    for (let j = 0; j < k; j++) {
      if (i === 0) {
        curr[j] = nums[i] % k === j
      } else {
        curr[j] = prev[normalize(j - nums[i])] || ((nums[i] + nums[i - 1]) % k === j) || false
      }

      if (i >= 1 && j === 0 && curr[j]) return true
    }

    prev = curr
  }

  return false
};
// @lc code=end

// console.log(checkSubarraySum([23,2,4,6,6], 7))
