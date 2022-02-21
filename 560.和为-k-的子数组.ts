/*
 * @lc app=leetcode.cn id=560 lang=typescript
 *
 * [560] 和为 K 的子数组
 *
 * https://leetcode-cn.com/problems/subarray-sum-equals-k/description/
 *
 * algorithms
 * Medium (44.76%)
 * Likes:    1320
 * Dislikes: 0
 * Total Accepted:    185.4K
 * Total Submissions: 414.1K
 * Testcase Example:  '[1,1,1]\n2'
 *
 * 给你一个整数数组 nums 和一个整数 k ，请你统计并返回该数组中和为 k 的连续子数组的个数。
 *
 *
 *
 * 示例 1：
 *
 *
 * 输入：nums = [1,1,1], k = 2
 * 输出：2
 *
 *
 * 示例 2：
 *
 *
 * 输入：nums = [1,2,3], k = 3
 * 输出：2
 *
 *
 *
 *
 * 提示：
 *
 *
 * 1 <= nums.length <= 2 * 10^4
 * -1000 <= nums[i] <= 1000
 * -10^7 <= k <= 10^7
 *
 *
 */

export
// @lc code=start
function subarraySum(nums: number[], k: number): number {
  const prefixSumCount: Record<number, number> = { 0: 1 }
  let prefixSum = 0
  let result = 0

  for (const n of nums) {
    prefixSum += n
    const target = prefixSum - k
    if (prefixSumCount[target]) {
      result += prefixSumCount[target]
    }
    prefixSumCount[prefixSum] = 1 + (prefixSumCount[prefixSum] || 0)
  }

  return result
}
// @lc code=end
