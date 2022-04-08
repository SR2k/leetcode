/*
 * @lc app=leetcode.cn id=259 lang=typescript
 *
 * [259] 较小的三数之和
 *
 * https://leetcode-cn.com/problems/3sum-smaller/description/
 *
 * algorithms
 * Medium (56.06%)
 * Likes:    104
 * Dislikes: 0
 * Total Accepted:    8.4K
 * Total Submissions: 14.9K
 * Testcase Example:  '[-2,0,1,3]\n2'
 *
 * 给定一个长度为 n 的整数数组和一个目标值 target ，寻找能够使条件 nums[i] + nums[j] + nums[k] < target
 * 成立的三元组  i, j, k 个数（0 <= i < j < k < n）。
 *
 *
 *
 * 示例 1：
 *
 *
 * 输入: nums = [-2,0,1,3], target = 2
 * 输出: 2
 * 解释: 因为一共有两个三元组满足累加和小于 2:
 * [-2,0,1]
 * ⁠    [-2,0,3]
 *
 *
 * 示例 2：
 *
 *
 * 输入: nums = [], target = 0
 * 输出: 0
 *
 * 示例 3：
 *
 *
 * 输入: nums = [0], target = 0
 * 输出: 0
 *
 *
 *
 * 提示:
 *
 *
 * n == nums.length
 * 0 <= n <= 3500
 * -100 <= nums[i] <= 100
 * -100 <= target <= 100
 *
 *
 */

export // @lc code=start
function threeSumSmaller(nums: number[], target: number): number {
  nums.sort((a, b) => a - b)
  let result = 0

  for (let i = 0; i < nums.length; i++) {
    let j = i + 1; let
      k = nums.length - 1

    while (j < k) {
      while (j < k && nums[i] + nums[j] + nums[k] >= target) {
        k -= 1
      }
      if (j === k) {
        break
      }
      result += k - j
      j += 1
    }
  }

  return result
}
// @lc code=end
