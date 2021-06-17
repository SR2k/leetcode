/*
 * @lc app=leetcode.cn id=209 lang=typescript
 *
 * [209] 长度最小的子数组
 *
 * https://leetcode-cn.com/problems/minimum-size-subarray-sum/description/
 *
 * algorithms
 * Medium (45.84%)
 * Likes:    637
 * Dislikes: 0
 * Total Accepted:    143.3K
 * Total Submissions: 311.9K
 * Testcase Example:  '7\n[2,3,1,2,4,3]'
 *
 * 给定一个含有 n 个正整数的数组和一个正整数 target 。
 * 
 * 找出该数组中满足其和 ≥ target 的长度最小的 连续子数组 [numsl, numsl+1, ..., numsr-1, numsr]
 * ，并返回其长度。如果不存在符合条件的子数组，返回 0 。
 * 
 * 
 * 
 * 示例 1：
 * 
 * 
 * 输入：target = 7, nums = [2,3,1,2,4,3]
 * 输出：2
 * 解释：子数组 [4,3] 是该条件下的长度最小的子数组。
 * 
 * 
 * 示例 2：
 * 
 * 
 * 输入：target = 4, nums = [1,4,4]
 * 输出：1
 * 
 * 
 * 示例 3：
 * 
 * 
 * 输入：target = 11, nums = [1,1,1,1,1,1,1,1]
 * 输出：0
 * 
 * 
 * 
 * 
 * 提示：
 * 
 * 
 * 1 
 * 1 
 * 1 
 * 
 * 
 * 
 * 
 * 进阶：
 * 
 * 
 * 如果你已经实现 O(n) 时间复杂度的解法, 请尝试设计一个 O(n log(n)) 时间复杂度的解法。
 * 
 * 
 */

// @lc code=start
// const getSum = (perfixSum: number[], l: number, r: number) => {
//   if (l === 0) return perfixSum[r]
//   return perfixSum[r] - perfixSum[l - 1]
// }

// const findFirstSumGETarget = (prefixSum: number[], n: number, target: number) => {
//   let left = 0, right = n
//   while (left < right - 1) {
//     const middle = ~~((left + right) / 2)
//     if (getSum(prefixSum, middle, n) < target) {
//       right = middle
//     } else {
//       left = middle
//     }
//   }

//   if (getSum(prefixSum, right, n) >= target) return right
//   if (getSum(prefixSum, left, n) >= target) return left

//   return -1
// }

// function minSubArrayLen(target: number, nums: number[]): number {
//   if (nums.length === 1) return nums[0] >= target ? 1 : 0

//   const prefixSum = [nums[0]]
//   let ret = Infinity

//   for (let i = 0; i < nums.length; i++) {
//     if (i === 0) {
//       prefixSum[i] = nums[i]
//     } else {
//       prefixSum[i] = prefixSum[i - 1] + nums[i]
//     }

//     const firstSumGETarget = findFirstSumGETarget(prefixSum, i, target)
//     if (firstSumGETarget !== -1) {
//       ret = Math.min(i - firstSumGETarget + 1, ret)
//     }
//   }

//   if (ret === Infinity) return 0
//   return ret
// };

function minSubArrayLen(target: number, nums: number[]): number {
  let ret = Infinity
  let left = 0, right = 0
  let sum = nums[0]

  while (right < nums.length) {
    if (sum >= target) {
      if (left === right) return 1
      ret = Math.min(ret, right - left + 1)
      sum -= nums[left]
      left++
    } else {
      right++
      sum += nums[right]
    }
  }

  if (ret === Infinity) return 0
  return ret
};
// @lc code=end

