/*
 * @lc app=leetcode.cn id=474 lang=javascript
 *
 * [474] 一和零
 *
 * https://leetcode-cn.com/problems/ones-and-zeroes/description/
 *
 * algorithms
 * Medium (56.42%)
 * Likes:    390
 * Dislikes: 0
 * Total Accepted:    40.4K
 * Total Submissions: 71.6K
 * Testcase Example:  '["10","0001","111001","1","0"]\n5\n3'
 *
 * 给你一个二进制字符串数组 strs 和两个整数 m 和 n 。
 * 
 * 
 * 请你找出并返回 strs 的最大子集的大小，该子集中 最多 有 m 个 0 和 n 个 1 。
 * 
 * 如果 x 的所有元素也是 y 的元素，集合 x 是集合 y 的 子集 。
 * 
 * 
 * 
 * 
 * 示例 1：
 * 
 * 
 * 输入：strs = ["10", "0001", "111001", "1", "0"], m = 5, n = 3
 * 输出：4
 * 解释：最多有 5 个 0 和 3 个 1 的最大子集是 {"10","0001","1","0"} ，因此答案是 4 。
 * 其他满足题意但较小的子集包括 {"0001","1"} 和 {"10","1","0"} 。{"111001"} 不满足题意，因为它含 4 个 1
 * ，大于 n 的值 3 。
 * 
 * 
 * 示例 2：
 * 
 * 
 * 输入：strs = ["10", "0", "1"], m = 1, n = 1
 * 输出：2
 * 解释：最大的子集是 {"0", "1"} ，所以答案是 2 。
 * 
 * 
 * 
 * 
 * 提示：
 * 
 * 
 * 1 
 * 1 
 * strs[i] 仅由 '0' 和 '1' 组成
 * 1 
 * 
 * 
 */

// @lc code=start
/**
 * @param {string[]} strs
 * @param {number} m
 * @param {number} n
 * @return {number}
 */
var findMaxForm = function(strs, m, n) {
  if (!strs || !strs.length || !m || !n) return 0

  const len = l = strs.length
  const dp = []

  for (let i = 0; i < len; i++) {
    const str = strs[i]
    let v0 = 0
    let v1 = 0
    for (const char of str) {
      if (char === '0') v0++
      if (char === '1') v1++
    }

    dp[i] = []

    for (let j = 0; j <= m; j++) {
      dp[i][j] = []

      for (let k = 0; k <= n; k++) {
        if (i === 0) {
          dp[i][j][k] = v0 <= j && v1 <= k ? 1 : 0
        } else if (v0 > j || v1 > k) {
          dp[i][j][k] = dp[i - 1][j][k]
        } else {
          dp[i][j][k] = Math.max(
            // 取
            dp[i - 1][j - v0][k - v1] + 1,
            // 不取
            dp[i - 1][j][k],
          )
        }
      }
    }
  }

  return dp[len - 1][m][n]
};
// @lc code=end
