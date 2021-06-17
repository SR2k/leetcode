/*
 * @lc app=leetcode.cn id=259 lang=javascript
 *
 * [259] 较小的三数之和
 *
 * https://leetcode-cn.com/problems/3sum-smaller/description/
 *
 * algorithms
 * Medium (57.55%)
 * Likes:    76
 * Dislikes: 0
 * Total Accepted:    5.7K
 * Total Submissions: 9.8K
 * Testcase Example:  '[-2,0,1,3]\n2'
 *
 * 给定一个长度为 n 的整数数组和一个目标值 target，寻找能够使条件 nums[i] + nums[j] + nums[k] < target
 * 成立的三元组  i, j, k 个数（0 <= i < j < k < n）。
 * 
 * 示例：
 * 
 * 输入: nums = [-2,0,1,3], target = 2
 * 输出: 2 
 * 解释: 因为一共有两个三元组满足累加和小于 2:
 * [-2,0,1]
 * ⁠    [-2,0,3]
 * 
 * 
 * 进阶：是否能在 O(n^2) 的时间复杂度内解决？
 * 
 */

// @lc code=start
/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
var threeSumSmaller = function(nums, target) {
  nums.sort((a, b) => a - b)
  let count = 0

  for (let i = 0; i < nums.length - 2; i++) {
    let left = i + 1, right = nums.length - 1

    while (left < right) {
      const sum = nums[i] + nums[left] + nums[right]
      if (sum < target) {
        count += right - left
        left++
      } else {
        right--
      }
    }
  }

  return count
};
// @lc code=end

