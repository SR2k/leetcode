/*
 * @lc app=leetcode.cn id=978 lang=javascript
 *
 * [978] 最长湍流子数组
 *
 * https://leetcode-cn.com/problems/longest-turbulent-subarray/description/
 *
 * algorithms
 * Medium (47.21%)
 * Likes:    164
 * Dislikes: 0
 * Total Accepted:    41K
 * Total Submissions: 86.8K
 * Testcase Example:  '[9,4,2,10,7,8,8,1,9]'
 *
 * 当 A 的子数组 A[i], A[i+1], ..., A[j] 满足下列条件时，我们称其为湍流子数组：
 * 
 * 
 * 若 i <= k < j，当 k 为奇数时， A[k] > A[k+1]，且当 k 为偶数时，A[k] < A[k+1]；
 * 或 若 i <= k < j，当 k 为偶数时，A[k] > A[k+1] ，且当 k 为奇数时， A[k] < A[k+1]。
 * 
 * 
 * 也就是说，如果比较符号在子数组中的每个相邻元素对之间翻转，则该子数组是湍流子数组。
 * 
 * 返回 A 的最大湍流子数组的长度。
 * 
 * 
 * 
 * 示例 1：
 * 
 * 输入：[9,4,2,10,7,8,8,1,9]
 * 输出：5
 * 解释：(A[1] > A[2] < A[3] > A[4] < A[5])
 * 
 * 
 * 示例 2：
 * 
 * 输入：[4,8,12,16]
 * 输出：2
 * 
 * 
 * 示例 3：
 * 
 * 输入：[100]
 * 输出：1
 * 
 * 
 * 
 * 
 * 提示：
 * 
 * 
 * 1 <= A.length <= 40000
 * 0 <= A[i] <= 10^9
 * 
 * 
 */

// @lc code=start
/**
 * @param {number[]} arr
 * @return {number}
 */
var maxTurbulenceSize = function(arr) {
  if (arr.length === 1) return 1

  const dp = [[1, 1]]

  let max = 0

  for (let i = 1; i < arr.length; i++) {
    dp[i] = [
      // 当前上升
      arr[i] > arr[i - 1] ? dp[i - 1][1] + 1 : 1,
      // 当前下降
      arr[i - 1] > arr[i] ? dp[i - 1][0] + 1 : 1,
    ]

    max = Math.max(max, dp[i][0], dp[i][1])
  }

  return max
};
// @lc code=end

