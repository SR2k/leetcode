/*
 * @lc app=leetcode.cn id=344 lang=typescript
 *
 * [344] 反转字符串
 *
 * https://leetcode.cn/problems/reverse-string/description/
 *
 * algorithms
 * Easy (79.00%)
 * Likes:    646
 * Dislikes: 0
 * Total Accepted:    597.3K
 * Total Submissions: 756K
 * Testcase Example:  '["h","e","l","l","o"]'
 *
 * 编写一个函数，其作用是将输入的字符串反转过来。输入字符串以字符数组 s 的形式给出。
 *
 * 不要给另外的数组分配额外的空间，你必须原地修改输入数组、使用 O(1) 的额外空间解决这一问题。
 *
 *
 *
 * 示例 1：
 *
 *
 * 输入：s = ["h","e","l","l","o"]
 * 输出：["o","l","l","e","h"]
 *
 *
 * 示例 2：
 *
 *
 * 输入：s = ["H","a","n","n","a","h"]
 * 输出：["h","a","n","n","a","H"]
 *
 *
 *
 * 提示：
 *
 *
 * 1 <= s.length <= 10^5
 * s[i] 都是 ASCII 码表中的可打印字符
 *
 *
 */

export
// @lc code=start
function reverseString(s: string[]): void {
  let i = 0, j = s.length - 1
  while (i < j) {
    swap(s, i++, j--)
  }
}

function swap(arr: any[], i: number, j: number) {
  const temp = arr[i]
  arr[i] = arr[j]
  arr[j] = temp
}
// @lc code=end
