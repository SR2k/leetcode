/*
 * @lc app=leetcode.cn id=31 lang=typescript
 *
 * [31] 下一个排列
 *
 * https://leetcode-cn.com/problems/next-permutation/description/
 *
 * algorithms
 * Medium (37.26%)
 * Likes:    1491
 * Dislikes: 0
 * Total Accepted:    248.8K
 * Total Submissions: 668K
 * Testcase Example:  '[1,2,3]'
 *
 * 实现获取 下一个排列 的函数，算法需要将给定数字序列重新排列成字典序中下一个更大的排列（即，组合出下一个更大的整数）。
 *
 * 如果不存在下一个更大的排列，则将数字重新排列成最小的排列（即升序排列）。
 *
 * 必须 原地 修改，只允许使用额外常数空间。
 *
 *
 *
 * 示例 1：
 *
 *
 * 输入：nums = [1,2,3]
 * 输出：[1,3,2]
 *
 *
 * 示例 2：
 *
 *
 * 输入：nums = [3,2,1]
 * 输出：[1,2,3]
 *
 *
 * 示例 3：
 *
 *
 * 输入：nums = [1,1,5]
 * 输出：[1,5,1]
 *
 *
 * 示例 4：
 *
 *
 * 输入：nums = [1]
 * 输出：[1]
 *
 *
 *
 *
 * 提示：
 *
 *
 * 1 <= nums.length <= 100
 * 0 <= nums[i] <= 100
 *
 *
 */

export
// @lc code=start
function nextPermutation(nums: number[]): void {
  let p = nums.length - 1
  while (p >= 1 && nums[p - 1] >= nums[p]) {
    p -= 1
  }
  if (p === 0) {
    nums.reverse()
    return
  }

  let i = nums.length - 1
  while (nums[i] <= nums[p - 1]) {
    i -= 1
  }
  [nums[i], nums[p - 1]] = [nums[p - 1], nums[i]]

  let left = p
  let right = nums.length - 1
  while (left < right) {
    [nums[left], nums[right]] = [nums[right], nums[left]]
    left += 1
    right -= 1
  }
}
// @lc code=end
