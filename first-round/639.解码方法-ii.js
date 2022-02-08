/*
 * @lc app=leetcode.cn id=639 lang=javascript
 *
 * [639] 解码方法 II
 *
 * https://leetcode-cn.com/problems/decode-ways-ii/description/
 *
 * algorithms
 * Hard (30.14%)
 * Likes:    83
 * Dislikes: 0
 * Total Accepted:    3.6K
 * Total Submissions: 11.8K
 * Testcase Example:  '"*"'
 *
 * 一条包含字母 A-Z 的消息通过以下的方式进行了编码：
 * 
 * 'A' -> 1
 * 'B' -> 2
 * ...
 * 'Z' -> 26
 * 
 * 
 * 除了上述的条件以外，现在加密字符串可以包含字符 '*'了，字符'*'可以被当做1到9当中的任意一个数字。
 * 
 * 给定一条包含数字和字符'*'的加密信息，请确定解码方法的总数。
 * 
 * 同时，由于结果值可能会相当的大，所以你应当对10^9 + 7取模。（翻译者标注：此处取模主要是为了防止溢出）
 * 
 * 示例 1 :
 * 
 * 输入: "*"
 * 输出: 9
 * 解释: 加密的信息可以被解密为: "A", "B", "C", "D", "E", "F", "G", "H", "I".
 * 
 * 
 * 示例 2 :
 * 
 * 输入: "1*"
 * 输出: 9 + 9 = 18（翻译者标注：这里1*可以分解为1,* 或者当做1*来处理，所以结果是9+9=18）
 * 
 * 
 * 说明 :
 * 
 * 
 * 输入的字符串长度范围是 [1, 10^5]。
 * 输入的字符串只会包含字符 '*' 和 数字'0' - '9'。
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
    // 1 - 9, * 都可以单独映射
    const canUseAsOneDigit = curr !== '0'
    // 1 和 * 可以和任意一位数组合
    // 2 可以和 0 - 6 组合
    const canUseAsTwoDigit = (curr === '*' || pre === '*')
      || pre === '1'
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

