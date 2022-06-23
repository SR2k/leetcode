/*
 * @lc app=leetcode.cn id=698 lang=typescript
 *
 * [698] 划分为k个相等的子集
 *
 * https://leetcode.cn/problems/partition-to-k-equal-sum-subsets/description/
 *
 * algorithms
 * Medium (41.69%)
 * Likes:    594
 * Dislikes: 0
 * Total Accepted:    51.2K
 * Total Submissions: 122.8K
 * Testcase Example:  '[4,3,2,3,5,2,1]\n4'
 *
 * 给定一个整数数组  nums 和一个正整数 k，找出是否有可能把这个数组分成 k 个非空子集，其总和都相等。
 *
 *
 *
 * 示例 1：
 *
 *
 * 输入： nums = [4, 3, 2, 3, 5, 2, 1], k = 4
 * 输出： True
 * 说明： 有可能将其分成 4 个子集（5），（1,4），（2,3），（2,3）等于总和。
 *
 * 示例 2:
 *
 *
 * 输入: nums = [1,2,3,4], k = 3
 * 输出: false
 *
 *
 *
 * 提示：
 *
 *
 * 1 <= k <= len(nums) <= 16
 * 0 < nums[i] < 10000
 * 每个元素的频率在 [1,4] 范围内
 *
 *
 */

// @lc code=start
function canPartitionKSubsets(nums: number[], k: number): boolean {
  const casesCount = 1 << nums.length

  const totalSum = nums.reduce((sum, curr) => sum + curr, 0)
  if (totalSum % k !== 0) return false
  const target = totalSum / k
  nums.sort((a, b) => a - b)

  if (nums[nums.length - 1] > target) return false

  const dp = new Array<boolean>(casesCount).fill(false)
  const sum = new Array<number>(casesCount).fill(0)
  dp[0] = true

  for (let i = 0; i < casesCount; i++) {
    for (let j = 0; j < nums.length; j++) {
      if ((i & (1 << j)) === 0) {
        continue
      }

      const prev = i ^ (1 << j)
      if (!dp[prev]) {
        continue
      }

      if ((sum[prev] % target) + nums[j] <= target) {
        dp[i] = true
        sum[i] = sum[prev] + nums[j]
      } else {
        break
      }
    }

    // console.log(i.toString(2), dp[i], sum[i])
  }

  return dp[casesCount - 1]
}
// @lc code=end

console.log(canPartitionKSubsets([4, 3, 2, 3, 5, 2, 1], 4))
console.log(canPartitionKSubsets([1, 2, 3, 4], 3))
console.log(canPartitionKSubsets([1, 2, 3, 3], 3))
console.log(canPartitionKSubsets([14], 7))
console.log(canPartitionKSubsets([2, 2, 5, 5], 7))
