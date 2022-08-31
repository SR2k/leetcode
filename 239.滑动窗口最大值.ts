/*
 * @lc app=leetcode.cn id=239 lang=typescript
 *
 * [239] 滑动窗口最大值
 *
 * https://leetcode.cn/problems/sliding-window-maximum/description/
 *
 * algorithms
 * Hard (50.02%)
 * Likes:    1816
 * Dislikes: 0
 * Total Accepted:    347.2K
 * Total Submissions: 694.1K
 * Testcase Example:  '[1,3,-1,-3,5,3,6,7]\n3'
 *
 * 给你一个整数数组 nums，有一个大小为 k 的滑动窗口从数组的最左侧移动到数组的最右侧。你只可以看到在滑动窗口内的 k
 * 个数字。滑动窗口每次只向右移动一位。
 *
 * 返回 滑动窗口中的最大值 。
 *
 *
 *
 * 示例 1：
 *
 *
 * 输入：nums = [1,3,-1,-3,5,3,6,7], k = 3
 * 输出：[3,3,5,5,6,7]
 * 解释：
 * 滑动窗口的位置                最大值
 * ---------------               -----
 * [1  3  -1] -3  5  3  6  7       3
 * ⁠1 [3  -1  -3] 5  3  6  7       3
 * ⁠1  3 [-1  -3  5] 3  6  7       5
 * ⁠1  3  -1 [-3  5  3] 6  7       5
 * ⁠1  3  -1  -3 [5  3  6] 7       6
 * ⁠1  3  -1  -3  5 [3  6  7]      7
 *
 *
 * 示例 2：
 *
 *
 * 输入：nums = n
 * 输出：[1]
 *
 *
 *
 *
 * 提示：
 *
 *
 * 1 <= nums.length <= 10^5
 * -10^4 <= nums[i] <= 10^4
 * 1 <= k <= nums.length
 *
 *
 */

export
// @lc code=start
function maxSlidingWindow(nums: number[], k: number): number[] {
  const queue: number[] = []
  const result: number[] = []

  for (let i = 0; i < nums.length; i++) {
    while (queue.length && i - queue[0] + 1 > k) {
      queue.shift()
    }

    const n = nums[i]
    while (queue.length && nums[queue.at(-1)!] <= n) {
      queue.pop()
    }
    queue.push(i)

    if (i >= k - 1) {
      result.push(nums[queue[0]])
    }
  }

  return result
}
// @lc code=end
