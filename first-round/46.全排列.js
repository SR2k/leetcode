/*
 * @lc app=leetcode.cn id=46 lang=javascript
 *
 * [46] 全排列
 *
 * https://leetcode-cn.com/problems/permutations/description/
 *
 * algorithms
 * Medium (77.89%)
 * Likes:    1355
 * Dislikes: 0
 * Total Accepted:    321.4K
 * Total Submissions: 412.6K
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
 * 1 
 * -10 
 * nums 中的所有整数 互不相同
 * 
 * 
 */

// @lc code=start
/**
 * @param {number[]} nums
 * @return {number[][]}
 */
var permute = function(nums) {
  const dfs = (index, currentPermute) => {
    if (index === nums.length) return currentPermute

    const newPermute = []
    currentPermute.forEach(x => {
      for (let i = 0; i < x.length; i++) {
        const newArr = [...x]
        newArr.splice(i, 0, nums[index])
        newPermute.push(newArr)
      }
      newPermute.push([...x, nums[index]])
    })

    return dfs(index + 1, newPermute)
  }

  return dfs(1, [[nums[0]]])
};
// @lc code=end

