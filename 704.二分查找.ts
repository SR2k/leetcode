/*
 * @lc app=leetcode.cn id=704 lang=typescript
 *
 * [704] 二分查找
 *
 * https://leetcode.cn/problems/binary-search/description/
 *
 * algorithms
 * Easy (54.40%)
 * Likes:    837
 * Dislikes: 0
 * Total Accepted:    606.6K
 * Total Submissions: 1.1M
 * Testcase Example:  '[-1,0,3,5,9,12]\n9'
 *
 * 给定一个 n 个元素有序的（升序）整型数组 nums 和一个目标值 target  ，写一个函数搜索 nums 中的
 * target，如果目标值存在返回下标，否则返回 -1。
 *
 *
 * 示例 1:
 *
 * 输入: nums = [-1,0,3,5,9,12], target = 9
 * 输出: 4
 * 解释: 9 出现在 nums 中并且下标为 4
 *
 *
 * 示例 2:
 *
 * 输入: nums = [-1,0,3,5,9,12], target = 2
 * 输出: -1
 * 解释: 2 不存在 nums 中因此返回 -1
 *
 *
 *
 *
 * 提示：
 *
 *
 * 你可以假设 nums 中的所有元素是不重复的。
 * n 将在 [1, 10000]之间。
 * nums 的每个元素都将在 [-9999, 9999]之间。
 *
 *
 */

// @lc code=start
function search(nums: number[], target: number): number {
  if (!nums.length) return -1

  let left = 0, right = nums.length - 1

  while (left + 1 < right) {
    const middle = Math.floor((left + right) / 2)

    if (nums[middle] === target) {
      return middle
    } else if (nums[middle] > target) {
      right = middle
    } else {
      left = middle
    }
  }

  if (nums[left] === target) return left
  if (nums[right] === target) return right
  return -1
}
// @lc code=end
