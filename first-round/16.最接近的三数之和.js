/*
 * @lc app=leetcode.cn id=16 lang=javascript
 *
 * [16] 最接近的三数之和
 *
 * https://leetcode-cn.com/problems/3sum-closest/description/
 *
 * algorithms
 * Medium (45.96%)
 * Likes:    779
 * Dislikes: 0
 * Total Accepted:    216.4K
 * Total Submissions: 470.9K
 * Testcase Example:  '[-1,2,1,-4]\n1'
 *
 * 给定一个包括 n 个整数的数组 nums 和 一个目标值 target。找出 nums 中的三个整数，使得它们的和与 target
 * 最接近。返回这三个数的和。假定每组输入只存在唯一答案。
 * 
 * 
 * 
 * 示例：
 * 
 * 输入：nums = [-1,2,1,-4], target = 1
 * 输出：2
 * 解释：与 target 最接近的和是 2 (-1 + 2 + 1 = 2) 。
 * 
 * 
 * 
 * 
 * 提示：
 * 
 * 
 * 3 <= nums.length <= 10^3
 * -10^3 <= nums[i] <= 10^3
 * -10^4 <= target <= 10^4
 * 
 * 
 */

// @lc code=start
/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
var threeSumClosest = function(nums, target) {
  nums.sort((a, b) => a - b)

  let currSum = Infinity
  let minDelta = Number.MAX_SAFE_INTEGER

  // console.log(nums)

  for (let i = 0; i < nums.length - 2; i++) {
    // console.log(`iterating nums[${i}] = ${nums[i]}`)

    let left = i + 1
    let right = nums.length - 1
    const a = nums[i]

    while (left < right) {
      // console.log(`iterating nums[${left}] = ${nums[left]}, nums[${right}] = ${nums[right]}`)
      const sum = a + nums[left] + nums[right]
      const delta = Math.abs(sum - target)
      if (delta === 0) return target

      if (delta < minDelta) {
        minDelta = delta
        currSum = sum
      }

      // console.log(`sum=${sum}`, `currSum=${currSum}`, `minDelta=${minDelta}`)

      if (sum < target) {
        while (nums[left] === nums[left + 1]) left++
        left++
      } else {
        while (nums[right] === nums[right - 1]) right--
        right--
      }
    }
  }

  return currSum
};
// @lc code=end

// console.log(threeSumClosest([-1,0,1,1,55], 3))
