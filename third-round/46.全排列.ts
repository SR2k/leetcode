/*
 * @lc app=leetcode.cn id=46 lang=typescript
 *
 * [46] 全排列
 *
 * https://leetcode-cn.com/problems/permutations/description/
 *
 * algorithms
 * Medium (78.49%)
 * Likes:    1763
 * Dislikes: 0
 * Total Accepted:    506.5K
 * Total Submissions: 645.3K
 * Testcase Example:  '[1,2,3]'
 *
 * 给定一个不含重复数字的数组 nums ，返回其 所有可能的全排列 。你可以 按任意顺序 返回答案。
 *
 *
 *
 * 示例 1：
 *
 *
 * 输入：nums = [1,2,3]
 * 输出：[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
 *
 *
 * 示例 2：
 *
 *
 * 输入：nums = [0,1]
 * 输出：[[0,1],[1,0]]
 *
 *
 * 示例 3：
 *
 *
 * 输入：nums = [1]
 * 输出：[[1]]
 *
 *
 *
 *
 * 提示：
 *
 *
 * 1 <= nums.length <= 6
 * -10 <= nums[i] <= 10
 * nums 中的所有整数 互不相同
 *
 *
 */

export
// @lc code=start
function permute(nums: number[]): number[][] {
  const result: number[][] = []

  function helper(i: number) {
    if (i >= nums.length) {
      result.push([...nums])
      return
    }

    helper(i + 1)

    for (let j = i + 1; j < nums.length; j++) {
      swap(nums, i, j)
      helper(i + 1)
      swap(nums, i, j)
    }
  }
  helper(0)

  return result
}

function swap(arr: any[], i: number, j: number) {
  [arr[i], arr[j]] = [arr[j], arr[i]]
}
// @lc code=end

// function permute(nums: number[]): number[][] {
//   const result: number[][] = []

//   function helper(i: number) {
//     if (i >= nums.length) {
//       result.push([...nums])
//       return
//     }

//     helper(i + 1)

//     for (let j = i + 1; j < nums.length; j++) {
//       if (nums[i] !== nums[j]) {
//         [nums[i], nums[j]] = [nums[j], nums[i]]
//         helper(i + 1);
//         [nums[i], nums[j]] = [nums[j], nums[i]]
//       }
//     }
//   }
//   helper(0)

//   return result
// }
