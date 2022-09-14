/*
 * @lc app=leetcode.cn id=540 lang=typescript
 *
 * [540] 有序数组中的单一元素
 *
 * https://leetcode.cn/problems/single-element-in-a-sorted-array/description/
 *
 * algorithms
 * Medium (60.73%)
 * Likes:    545
 * Dislikes: 0
 * Total Accepted:    104.6K
 * Total Submissions: 172.3K
 * Testcase Example:  '[1,1,2,3,3,4,4,8,8]'
 *
 * 给你一个仅由整数组成的有序数组，其中每个元素都会出现两次，唯有一个数只会出现一次。
 *
 * 请你找出并返回只出现一次的那个数。
 *
 * 你设计的解决方案必须满足 O(log n) 时间复杂度和 O(1) 空间复杂度。
 *
 *
 *
 * 示例 1:
 *
 *
 * 输入: nums = [1,1,2,3,3,4,4,8,8]
 * 输出: 2
 *
 *
 * 示例 2:
 *
 *
 * 输入: nums =  [3,3,7,7,10,11,11]
 * 输出: 10
 *
 *
 *
 *
 *
 *
 * 提示:
 *
 *
 * 1 <= nums.length <= 10^5
 * 0 <= nums[i] <= 10^5
 *
 *
 */

export
// @lc code=start
function singleNonDuplicate(nums: number[]): number {
  let left = 0, right = nums.length - 1

  while (left + 1 < right) {
    const middle = (left + right) >> 1

    if (check(middle, nums)) {
      left = middle
    } else {
      right = middle
    }
  }

  const ret = [left, right].filter((x) => !check(x, nums))
  if (!ret.length) return nums.at(-1)!
  return nums[Math.min(...ret)]
}

function check(n: number, nums: number[]) {
  if (n & 1) {
    return nums[n - 1] === nums[n]
  }
  return n + 1 < nums.length && nums[n + 1] === nums[n]
}
// @lc code=end
