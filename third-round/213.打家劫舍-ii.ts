/*
 * @lc app=leetcode.cn id=213 lang=typescript
 *
 * [213] 打家劫舍 II
 *
 * https://leetcode-cn.com/problems/house-robber-ii/description/
 *
 * algorithms
 * Medium (43.59%)
 * Likes:    932
 * Dislikes: 0
 * Total Accepted:    206.2K
 * Total Submissions: 472.8K
 * Testcase Example:  '[2,3,2]'
 *
 * 你是一个专业的小偷，计划偷窃沿街的房屋，每间房内都藏有一定的现金。这个地方所有的房屋都 围成一圈
 * ，这意味着第一个房屋和最后一个房屋是紧挨着的。同时，相邻的房屋装有相互连通的防盗系统，如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警 。
 *
 * 给定一个代表每个房屋存放金额的非负整数数组，计算你 在不触动警报装置的情况下 ，今晚能够偷窃到的最高金额。
 *
 *
 *
 * 示例 1：
 *
 *
 * 输入：nums = [2,3,2]
 * 输出：3
 * 解释：你不能先偷窃 1 号房屋（金额 = 2），然后偷窃 3 号房屋（金额 = 2）, 因为他们是相邻的。
 *
 *
 * 示例 2：
 *
 *
 * 输入：nums = [1,2,3,1]
 * 输出：4
 * 解释：你可以先偷窃 1 号房屋（金额 = 1），然后偷窃 3 号房屋（金额 = 3）。
 * 偷窃到的最高金额 = 1 + 3 = 4 。
 *
 * 示例 3：
 *
 *
 * 输入：nums = [1,2,3]
 * 输出：3
 *
 *
 *
 *
 * 提示：
 *
 *
 * 1 <= nums.length <= 100
 * 0 <= nums[i] <= 1000
 *
 *
 */

export
// @lc code=start
function rob(nums: number[]): number {
  if (nums.length === 1) return nums[0]

  const dpYes1 = [nums[0], nums[0]]
  const dpNo1 = [nums[1], 0]

  for (let i = 2; i < nums.length - 1; i++) {
    const n = nums[i]

    const yes1 = dpYes1[1] + n
    const no1 = Math.max(...dpYes1)
    dpYes1[0] = yes1
    dpYes1[1] = no1

    const yes2 = dpNo1[1] + n
    const no2 = Math.max(...dpNo1)
    dpNo1[0] = yes2
    dpNo1[1] = no2
  }

  const yesLast = dpNo1[1] + nums[nums.length - 1]
  const noLast = Math.max(...dpYes1, ...dpNo1)
  return Math.max(yesLast, noLast)
}
// @lc code=end
