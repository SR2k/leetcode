/*
 * @lc app=leetcode.cn id=283 lang=typescript
 *
 * [283] 移动零
 *
 * https://leetcode-cn.com/problems/move-zeroes/description/
 *
 * algorithms
 * Easy (64.03%)
 * Likes:    1395
 * Dislikes: 0
 * Total Accepted:    595.7K
 * Total Submissions: 930.4K
 * Testcase Example:  '[0,1,0,3,12]'
 *
 * 给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。
 *
 * 示例:
 *
 * 输入: [0,1,0,3,12]
 * 输出: [1,3,12,0,0]
 *
 * 说明:
 *
 *
 * 必须在原数组上操作，不能拷贝额外的数组。
 * 尽量减少操作次数。
 *
 *
 */

export
// @lc code=start
function moveZeroes(nums: number[]): void {
  let i = 0
  let p0 = 0

  while (p0 < nums.length) {
    while (p0 < nums.length && nums[p0] === 0) {
      p0 += 1
    }
    if (p0 === nums.length) return

    [nums[i], nums[p0]] = [nums[p0], nums[i]]
    i += 1
    p0 += 1
  }
}
// @lc code=end
