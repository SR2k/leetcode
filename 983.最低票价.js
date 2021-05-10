/*
 * @lc app=leetcode.cn id=983 lang=javascript
 *
 * [983] 最低票价
 */

// @lc code=start
/**
 * @param {number[]} days
 * @param {number[]} costs
 * @return {number}
 */
var mincostTickets = function(days, costs) {
  let daysIndex = days.length - 1
  const dp = []
  dp[366] = 0

  for (let i = days[days.length - 1]; i >= 1; i--) {
    if (dp[i] === days[daysIndex]) {
      daysIndex --
      const cost1Day = cost[0] + (dp[  ] || Number.MAX_SAFE_INTEGER)
      const cost7Day = cost[1] + (dp[i + 7] || Number.MAX_SAFE_INTEGER)
      const cost30Day = cost[2] + (dp[i + 30] || Number.MAX_SAFE_INTEGER)
      dp[i] = Math.min(cost1Day, cost7Day, cost30Day)
    } else {
      dp[i] = dp[i + 1]
    }

    if (daysIndex <= 0) break
  }

  return dp[1]
};
// @lc code=end

