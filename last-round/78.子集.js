/*
 * @lc app=leetcode.cn id=78 lang=javascript
 *
 * [78] 子集
 *
 * https://leetcode-cn.com/problems/subsets/description/
 *
 * algorithms
 * Medium (79.81%)
 * Likes:    1177
 * Dislikes: 0
 * Total Accepted:    247.9K
 * Total Submissions: 310.5K
 * Testcase Example:  '[1,2,3]'
 *
 * 给你一个整数数组 nums ，数组中的元素 互不相同 。返回该数组所有可能的子集（幂集）。
 * 
 * 解集 不能 包含重复的子集。你可以按 任意顺序 返回解集。
 * 
 * 
 * 
 * 示例 1：
 * 
 * 
 * 输入：nums = [1,2,3]
 * 输出：[[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
 * 
 * 
 * 示例 2：
 * 
 * 
 * 输入：nums = [0]
 * 输出：[[],[0]]
 * 
 * 
 * 
 * 
 * 提示：
 * 
 * 
 * 1 
 * -10 
 * nums 中的所有元素 互不相同
 * 
 * 
 */

// @lc code=start
/**
 * @param {number[]} nums
 * @return {number[][]}
 */
var subsets = function(nums) {
  // 1. 模拟
  // if (!nums.length) return nums

  // const ret = [[]]

  // for (let i = 0; i < nums.length; i++) {
  //   const newRet = ret.map(x => [...x, nums[i]])
  //   ret.push(...newRet)
  // }

  // return ret

  // 2. dfs
  const result = []

  const dfs = (index, currentSubset) => {
    if (index === nums.length) {
      result.push(currentSubset)
      return
    }

    // 本层选了
    dfs(index + 1, [...currentSubset])
    dfs(index + 1, [...currentSubset, nums[index]])
  }
  dfs(0, [])

  return result
};
// @lc code=end
