/*
 * @lc app=leetcode.cn id=15 lang=typescript
 *
 * [15] 三数之和
 *
 * https://leetcode.cn/problems/3sum/description/
 *
 * algorithms
 * Medium (35.70%)
 * Likes:    4904
 * Dislikes: 0
 * Total Accepted:    1M
 * Total Submissions: 2.9M
 * Testcase Example:  '[-1,0,1,2,-1,-4]'
 *
 * 给你一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？请你找出所有和为 0
 * 且不重复的三元组。
 *
 * 注意：答案中不可以包含重复的三元组。
 *
 *
 *
 * 示例 1：
 *
 *
 * 输入：nums = [-1,0,1,2,-1,-4]
 * 输出：[[-1,-1,2],[-1,0,1]]
 *
 *
 * 示例 2：
 *
 *
 * 输入：nums = []
 * 输出：[]
 *
 *
 * 示例 3：
 *
 *
 * 输入：nums = [0]
 * 输出：[]
 *
 *
 *
 *
 * 提示：
 *
 *
 * 0
 * -10^5
 *
 *
 */

export
// @lc code=start
function threeSum(nums: number[]): number[][] {
  nums.sort((a, b) => a - b)
  const result: number[][] = []

  for (let a = 0; a < nums.length - 2; a++) {
    if (a > 0 && nums[a] === nums[a - 1]) {
      continue
    }

    let c = nums.length - 1
    for (let b = a + 1; b < nums.length - 1; b++) {
      if (b > a + 1 && nums[b] === nums[b - 1]) {
        continue
      }
      while (b < c && nums[a] + nums[b] + nums[c] > 0) {
        c--
      }
      if (b === c) {
        break
      }
      if (nums[a] + nums[b] + nums[c] === 0) {
        result.push([nums[a], nums[b], nums[c]])
      }
    }
  }

  return result
}
// @lc code=end

console.log(threeSum([-1,0,1,2,-1,-4,-2,-3,3,0,4]))
