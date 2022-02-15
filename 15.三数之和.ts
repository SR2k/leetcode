/*
 * @lc app=leetcode.cn id=15 lang=typescript
 *
 * [15] 三数之和
 *
 * https://leetcode-cn.com/problems/3sum/description/
 *
 * algorithms
 * Medium (34.47%)
 * Likes:    4291
 * Dislikes: 0
 * Total Accepted:    793.2K
 * Total Submissions: 2.3M
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
function threeSum(nums: number[]): [number, number, number][] {
  if (nums.length < 3) return []

  const result: Array<[number, number, number]> = []
  nums.sort((a, b) => a - b) //  [-1,-1,-4,0,1,2]

  for (let i = 0; i < nums.length - 2; i++) {
    if (i > 0 && nums[i] === nums[i - 1]) {
      continue
    }

    let k = nums.length - 1
    for (let j = i + 1; j < nums.length - 1; j++) {
      if (j > i + 1 && nums[j] === nums[j - 1]) {
        continue
      }

      while (j < k && nums[i] + nums[j] + nums[k] > 0) {
        k -= 1
      }
      if (j === k) break

      if (nums[i] + nums[j] + nums[k] === 0) {
        result.push([nums[i], nums[j], nums[k]])
      }
    }
  }

  return result
}
// @lc code=end
