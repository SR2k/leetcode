/*
 * @lc app=leetcode.cn id=5 lang=javascript
 *
 * [5] 最长回文子串
 *
 * https://leetcode-cn.com/problems/longest-palindromic-substring/description/
 *
 * algorithms
 * Medium (34.11%)
 * Likes:    3606
 * Dislikes: 0
 * Total Accepted:    572.2K
 * Total Submissions: 1.7M
 * Testcase Example:  '"babad"'
 *
 * 给你一个字符串 s，找到 s 中最长的回文子串。
 * 
 * 
 * 
 * 示例 1：
 * 
 * 
 * 输入：s = "babad"
 * 输出："bab"
 * 解释："aba" 同样是符合题意的答案。
 * 
 * 
 * 示例 2：
 * 
 * 
 * 输入：s = "cbbd"
 * 输出："bb"
 * 
 * 
 * 示例 3：
 * 
 * 
 * 输入：s = "a"
 * 输出："a"
 * 
 * 
 * 示例 4：
 * 
 * 
 * 输入：s = "ac"
 * 输出："a"
 * 
 * 
 * 
 * 
 * 提示：
 * 
 * 
 * 1 
 * s 仅由数字和英文字母（大写和/或小写）组成
 * 
 * 
 */

// @lc code=start
/**
 * @param {string} s
 * @return {string}
 */
var longestPalindrome = function(s) {
  let maxSubStr = ''

  for (let i = 0; i < s.length; i += 0.5) {
    let left = Math.floor(i)
    let right = Math.ceil(i)

    while(left >= 0 && right <= s.length - 1) {
      if (s[left] !== s[right]) break

      const currentSubString = s.slice(left, right + 1)
      if (currentSubString.length > maxSubStr.length) {
        maxSubStr = currentSubString
      }

      left--
      right++
    }
  }

  return maxSubStr
};
// @lc code=end

// console.log(longestPalindrome('babad'))
// console.log(longestPalindrome('babbad'))
