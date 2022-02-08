/*
 * @lc app=leetcode.cn id=91 lang=javascript
 *
 * [91] 解码方法
 *
 * https://leetcode-cn.com/problems/decode-ways/description/
 *
 * algorithms
 * Medium (29.34%)
 * Likes:    838
 * Dislikes: 0
 * Total Accepted:    130.8K
 * Total Submissions: 445.8K
 * Testcase Example:  '"12"'
 *
 * 一条包含字母 A-Z 的消息通过以下映射进行了 编码 ：
 * 
 * 
 * 'A' -> 1
 * 'B' -> 2
 * ...
 * 'Z' -> 26
 * 
 * 
 * 要 解码 已编码的消息，所有数字必须基于上述映射的方法，反向映射回字母（可能有多种方法）。例如，"11106" 可以映射为：
 * 
 * 
 * "AAJF" ，将消息分组为 (1 1 10 6)
 * "KJF" ，将消息分组为 (11 10 6)
 * 
 * 
 * 注意，消息不能分组为  (1 11 06) ，因为 "06" 不能映射为 "F" ，这是由于 "6" 和 "06" 在映射中并不等价。
 * 
 * 给你一个只含数字的 非空 字符串 s ，请计算并返回 解码 方法的 总数 。
 * 
 * 题目数据保证答案肯定是一个 32 位 的整数。
 * 
 * 
 * 
 * 示例 1：
 * 
 * 
 * 输入：s = "12"
 * 输出：2
 * 解释：它可以解码为 "AB"（1 2）或者 "L"（12）。
 * 
 * 
 * 示例 2：
 * 
 * 
 * 输入：s = "226"
 * 输出：3
 * 解释：它可以解码为 "BZ" (2 26), "VF" (22 6), 或者 "BBF" (2 2 6) 。
 * 
 * 
 * 示例 3：
 * 
 * 
 * 输入：s = "0"
 * 输出：0
 * 解释：没有字符映射到以 0 开头的数字。
 * 含有 0 的有效映射是 'J' -> "10" 和 'T'-> "20" 。
 * 由于没有字符，因此没有有效的方法对此进行解码，因为所有数字都需要映射。
 * 
 * 
 * 示例 4：
 * 
 * 
 * 输入：s = "06"
 * 输出：0
 * 解释："06" 不能映射到 "F" ，因为字符串含有前导 0（"6" 和 "06" 在映射中并不等价）。
 * 
 * 
 * 
 * 提示：
 * 
 * 
 * 1 
 * s 只包含数字，并且可能包含前导零。
 * 
 * 
 */
// @lc code=start
/**
 * @param {string} s
 * @return {number}
 */
var numDecodings = function(s) {
  if (!s) return 0

  const GroupStrategies = {
    None: 0,
    SingleDigit: 1,
    DoubleDigit: 2,
    SingleOrDoubleDigit: 3,
  }
  
  // 判断当前数字可以怎么组合
  const strategyHelper = (curr, pre) => {
    // 1 - 9 都可以单独映射
    const canUseAsOneDigit = curr !== '0'
    // 1 可以和任意一位数组合
    // 2 可以和 0 - 6 组合
    const canUseAsTwoDigit = pre === '1'
      || (pre === '2' && ['0', '1', '2', '3', '4', '5', '6'].indexOf(curr) >= 0)
  
    if (canUseAsOneDigit && canUseAsTwoDigit) return GroupStrategies.SingleOrDoubleDigit
    if (canUseAsTwoDigit) return GroupStrategies.DoubleDigit
    if (canUseAsOneDigit) return GroupStrategies.SingleDigit
    return GroupStrategies.None
  }

  const dp = []

  const { length } = s
  for (let i = 0; i < length; i++) {
    const curr = s[i]
    const pre = s[i - 1]

    const strategy = strategyHelper(curr, pre)

    switch (strategy) {
      case GroupStrategies.SingleDigit:
        dp[i] = i === 0 ? 1 : dp[i - 1]
        break
      case GroupStrategies.DoubleDigit:
        dp[i] = i < 2 ? 1 : dp[i - 2]
        break
      case GroupStrategies.SingleOrDoubleDigit:
        dp[i] = i < 2 ? 2 : dp[i - 1] + dp[i - 2]
        break
      case GroupStrategies.None:
        return 0
    }
  }

  return dp[length - 1]
};

// @lc code=end

// console.log(numDecodings("12"))
// console.log(numDecodings("226"))
// console.log(numDecodings("0"))
// console.log(numDecodings("00006"))
