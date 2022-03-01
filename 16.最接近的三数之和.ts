/*
 * @lc app=leetcode.cn id=16 lang=typescript
 *
 * [16] 最接近的三数之和
 *
 * https://leetcode-cn.com/problems/3sum-closest/description/
 *
 * algorithms
 * Medium (45.89%)
 * Likes:    1039
 * Dislikes: 0
 * Total Accepted:    302.9K
 * Total Submissions: 660.1K
 * Testcase Example:  '[-1,2,1,-4]\n1'
 *
 * 给你一个长度为 n 的整数数组 nums 和 一个目标值 target。请你从 nums 中选出三个整数，使它们的和与 target 最接近。
 *
 * 返回这三个数的和。
 *
 * 假定每组输入只存在恰好一个解。
 *
 *
 *
 * 示例 1：
 *
 *
 * 输入：nums = [-1,2,1,-4], target = 1
 * 输出：2
 * 解释：与 target 最接近的和是 2 (-1 + 2 + 1 = 2) 。
 *
 *
 * 示例 2：
 *
 *
 * 输入：nums = [0,0,0], target = 1
 * 输出：0
 *
 *
 *
 *
 * 提示：
 *
 *
 * 3 <= nums.length <= 1000
 * -1000 <= nums[i] <= 1000
 * -10^4 <= target <= 10^4
 *
 *
 */

export
// @lc code=start
function threeSumClosest(nums: number[], target: number): number {
  nums.sort((a, b) => a - b)
  let result = Number.MAX_SAFE_INTEGER

  for (let i = 0; i < nums.length - 2; i++) {
    let k = nums.length - 1

    for (let j = i + 1; j < nums.length - 1; j++) {
      while (j < k && nums[i] + nums[j] + nums[k] > target) {
        result = closest(target, nums[i] + nums[j] + nums[k], result)
        k -= 1
      }
      if (j === k) break

      result = closest(target, nums[i] + nums[j] + nums[k], result)
    }
  }

  return result
}

function closest(target: number, a: number, b: number) {
  const absA = Math.abs(a - target), absB = Math.abs(b - target)

  if (absA < absB) {
    return a
  }
  return b
}
// @lc code=end

// function threeSumClosest(nums: number[], target: number): number {
//   nums.sort((a, b) => a - b)
//   let result = Infinity

//   for (let i = 0; i < nums.length - 2; i++) {
//     let j = i + 1; let
//       k = nums.length - 1

//     while (j < k) {
//       const sum = nums[i] + nums[j] + nums[k]
//       if (sum === target) return sum
//       if (Math.abs(sum - target) < Math.abs(result - target)) {
//         result = sum
//       }

//       if (sum > target) {
//         k -= 1
//       } else {
//         j += 1
//       }
//     }
//   }

//   return result
// }
