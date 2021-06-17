/*
 * @lc app=leetcode.cn id=467 lang=javascript
 *
 * [467] 环绕字符串中唯一的子字符串
 *
 * https://leetcode-cn.com/problems/unique-substrings-in-wraparound-string/description/
 *
 * algorithms
 * Medium (43.35%)
 * Likes:    149
 * Dislikes: 0
 * Total Accepted:    7.3K
 * Total Submissions: 16.8K
 * Testcase Example:  '"a"'
 *
 * 把字符串 s 看作是“abcdefghijklmnopqrstuvwxyz”的无限环绕字符串，所以 s
 * 看起来是这样的："...zabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcd....". 
 * 
 * 现在我们有了另一个字符串 p 。你需要的是找出 s 中有多少个唯一的 p 的非空子串，尤其是当你的输入是字符串 p ，你需要输出字符串 s 中 p
 * 的不同的非空子串的数目。 
 * 
 * 注意: p 仅由小写的英文字母组成，p 的大小可能超过 10000。
 * 
 * 
 * 
 * 示例 1:
 * 
 * 
 * 输入: "a"
 * 输出: 1
 * 解释: 字符串 S 中只有一个"a"子字符。
 * 
 * 
 * 
 * 
 * 示例 2:
 * 
 * 
 * 输入: "cac"
 * 输出: 2
 * 解释: 字符串 S 中的字符串“cac”只有两个子串“a”、“c”。.
 * 
 * 
 * 
 * 
 * 示例 3:
 * 
 * 
 * 输入: "zab"
 * 输出: 6
 * 解释: 在字符串 S 中有六个子串“z”、“a”、“b”、“za”、“ab”、“zab”。.
 * 
 * 
 * 
 * 
 */

// @lc code=start
/**
 * @param {string} p
 * @return {number}
 */
var findSubstringInWraproundString = function(p) {
  if (!p) return 0

  const judge = (prev, curr) => {
    if (prev === 'z') return curr === 'a'
    return prev.charCodeAt(0) === curr.charCodeAt(0) - 1
  }

  let prev = 1
  const map = {
    [p[0]]: 1
  }

  for (let i = 1; i < p.length; i++) {
    prev = judge(p[i - 1], p[i]) ? prev + 1 : 1
    map[p[i]] = Math.max(map[p[i]] || 0, prev)
  }

  let total = 0
  for (let k in map) total += map[k]

  return total
};
// @lc code=end

