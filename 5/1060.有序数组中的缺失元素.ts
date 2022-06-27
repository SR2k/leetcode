/*
 * @lc app=leetcode.cn id=1060 lang=typescript
 *
 * [1060] 有序数组中的缺失元素
 *
 * https://leetcode.cn/problems/missing-element-in-sorted-array/description/
 *
 * algorithms
 * Medium (53.43%)
 * Likes:    106
 * Dislikes: 0
 * Total Accepted:    8.1K
 * Total Submissions: 15.2K
 * Testcase Example:  '[4,7,9,10]\n1'
 *
 * 现有一个按 升序 排列的整数数组 nums ，其中每个数字都 互不相同 。
 *
 * 给你一个整数 k ，请你找出并返回从数组最左边开始的第 k 个缺失数字。
 *
 *
 *
 * 示例 1：
 *
 *
 * 输入：nums = [4,7,9,10], k = 1
 * 输出：5
 * 解释：第一个缺失数字为 5 。
 *
 *
 * 示例 2：
 *
 *
 * 输入：nums = [4,7,9,10], k = 3
 * 输出：8
 * 解释：缺失数字有 [5,6,8,...]，因此第三个缺失数字为 8 。
 *
 *
 * 示例 3：
 *
 *
 * 输入：nums = [1,2,4], k = 3
 * 输出：6
 * 解释：缺失数字有 [3,5,6,7,...]，因此第三个缺失数字为 6 。
 *
 *
 *
 *
 * 提示：
 *
 *
 * 1
 * 1
 * nums 按 升序 排列，其中所有元素 互不相同 。
 * 1
 *
 *
 *
 *
 * 进阶：你可以设计一个对数时间复杂度（即，O(log(n))）的解决方案吗？
 *
 */

// @lc code=start
function missingElement(nums: number[], k: number): number {
  let left = 0, right = nums.length - 1

  while (left + 1 < right) {
    const middle = Math.floor((left + right) / 2)

    const missedCount = (nums[middle] - nums[0]) - middle
    if (missedCount >= k) {
      right = middle
    } else {
      left = middle
    }
  }

  const rightCount = nums[right] - nums[0] - right

  if (rightCount >= k) {
    return nums[right] - (rightCount - k + 1)
  }
  return nums[right] + (k - rightCount)
}
// @lc code=end
