/*
 * @lc app=leetcode.cn id=1155 lang=javascript
 *
 * [1155] 掷骰子的N种方法
 *
 * https://leetcode-cn.com/problems/number-of-dice-rolls-with-target-sum/description/
 *
 * algorithms
 * Medium (47.72%)
 * Likes:    88
 * Dislikes: 0
 * Total Accepted:    7.3K
 * Total Submissions: 15.3K
 * Testcase Example:  '1\n6\n3'
 *
 * 这里有 d 个一样的骰子，每个骰子上都有 f 个面，分别标号为 1, 2, ..., f。
 * 
 * 我们约定：掷骰子的得到总点数为各骰子面朝上的数字的总和。
 * 
 * 如果需要掷出的总点数为 target，请你计算出有多少种不同的组合情况（所有的组合情况总共有 f^d 种），模 10^9 + 7 后返回。
 * 
 * 
 * 
 * 示例 1：
 * 
 * 输入：d = 1, f = 6, target = 3
 * 输出：1
 * 
 * 
 * 示例 2：
 * 
 * 输入：d = 2, f = 6, target = 7
 * 输出：6
 * 
 * 
 * 示例 3：
 * 
 * 输入：d = 2, f = 5, target = 10
 * 输出：1
 * 
 * 
 * 示例 4：
 * 
 * 输入：d = 1, f = 2, target = 3
 * 输出：0
 * 
 * 
 * 示例 5：
 * 
 * 输入：d = 30, f = 30, target = 500
 * 输出：222616187
 * 
 * 
 * 
 * 提示：
 * 
 * 
 * 1 <= d, f <= 30
 * 1 <= target <= 1000
 * 
 * 
 */

// @lc code=start
/**
 * @param {number} d
 * @param {number} f
 * @param {number} target
 * @return {number}
 */
var numRollsToTarget = function(d, f, target) {
  if (target < d || target > d * f) return 0

  const dp = []
  for (let i = 1; i <= d; i++) {
    dp[i] = []

    for (let j = i; j <= i * f; j++) {
      if (i === 1) {
        dp[i][j] = 1
      } else {
        dp[i][j] = 0

        for (let k = 1; k <= f; k++) {
          dp[i][j] += dp[i - 1][j - k] || 0
          dp[i][j] %= 1e9 + 7
        }
      }
    }
  }

  return dp[d][target]
};
// @lc code=end

