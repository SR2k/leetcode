/*
 * @lc app=leetcode.cn id=18 lang=typescript
 *
 * [18] 四数之和
 *
 * https://leetcode.cn/problems/4sum/description/
 *
 * algorithms
 * Medium (38.37%)
 * Likes:    1340
 * Dislikes: 0
 * Total Accepted:    360.2K
 * Total Submissions: 938.8K
 * Testcase Example:  '[1,0,-1,0,-2,2]\n0'
 *
 * 给你一个由 n 个整数组成的数组 nums ，和一个目标值 target 。请你找出并返回满足下述全部条件且不重复的四元组 [nums[a],
 * nums[b], nums[c], nums[d]] （若两个四元组元素一一对应，则认为两个四元组重复）：
 *
 *
 * 0 <= a, b, c, d < n
 * a、b、c 和 d 互不相同
 * nums[a] + nums[b] + nums[c] + nums[d] == target
 *
 *
 * 你可以按 任意顺序 返回答案 。
 *
 *
 *
 * 示例 1：
 *
 *
 * 输入：nums = [1,0,-1,0,-2,2], target = 0
 * 输出：[[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
 *
 *
 * 示例 2：
 *
 *
 * 输入：nums = [2,2,2,2,2], target = 8
 * 输出：[[2,2,2,2]]
 *
 *
 *
 *
 * 提示：
 *
 *
 * 1 <= nums.length <= 200
 * -10^9 <= nums[i] <= 10^9
 * -10^9 <= target <= 10^9
 *
 *
 */

export
// @lc code=start
function fourSum(nums: number[], target: number): number[][] {
  nums.sort((a, b) => a - b)
  const result: Array<[number, number, number, number]> = []

  for (let a = 0; a < nums.length - 3; a++) {
    if (a !== 0 && nums[a] === nums[a - 1]) {
      continue
    }

    for (let b = a + 1; b < nums.length - 2; b++) {
      if (b !== a + 1 && nums[b] === nums[b - 1]) {
        continue
      }

      const sumAB = nums[a] + nums[b]

      let d = nums.length - 1
      for (let c = b + 1; c < nums.length - 1; c++) {
        if (c !== b + 1 && nums[c] === nums[c - 1]) {
          continue
        }

        while (c < d && sumAB + nums[c] + nums[d] > target) {
          d--
        }
        if (c >= d) break

        if (sumAB + nums[c] + nums[d] === target) {
          result.push([nums[a], nums[b], nums[c], nums[d]])
        }
      }
    }
  }

  return result
}
// @lc code=end
