/*
 * @lc app=leetcode.cn id=1784 lang=typescript
 *
 * [1784] 检查二进制字符串字段
 *
 * https://leetcode-cn.com/problems/check-if-binary-string-has-at-most-one-segment-of-ones/description/
 *
 * algorithms
 * Easy (41.73%)
 * Likes:    9
 * Dislikes: 0
 * Total Accepted:    8.2K
 * Total Submissions: 19.5K
 * Testcase Example:  '"1001"'
 *
 * 给你一个二进制字符串 s ，该字符串 不含前导零 。
 * 
 * 如果 s 最多包含 一个由连续的 '1' 组成的字段 ，返回 true​​​ 。否则，返回 false 。
 * 
 * 
 * 
 * 示例 1：
 * 
 * 
 * 输入：s = "1001"
 * 输出：false
 * 解释：字符串中的 1 没有形成一个连续字段。
 * 
 * 
 * 示例 2：
 * 
 * 
 * 输入：s = "110"
 * 输出：true
 * 
 * 
 * 
 * 提示：
 * 
 * 
 * 1 
 * s[i]​​​​ 为 '0' 或 '1'
 * s[0] 为 '1'
 * 
 * 
 */

// @lc code=start
function checkOnesSegment(s: string): boolean {
  return s.indexOf('01') < 0
};
// @lc code=end
