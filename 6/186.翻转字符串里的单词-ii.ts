/*
 * @lc app=leetcode.cn id=186 lang=typescript
 *
 * [186] 翻转字符串里的单词 II
 *
 * https://leetcode.cn/problems/reverse-words-in-a-string-ii/description/
 *
 * algorithms
 * Medium (75.71%)
 * Likes:    81
 * Dislikes: 0
 * Total Accepted:    10.5K
 * Total Submissions: 13.9K
 * Testcase Example:  '["t","h","e"," ","s","k","y"," ","i","s"," ","b","l","u","e"]'
 *
 * 给定一个字符串，逐个翻转字符串中的每个单词。
 *
 * 示例：
 *
 * 输入: ["t","h","e"," ","s","k","y"," ","i","s"," ","b","l","u","e"]
 * 输出: ["b","l","u","e"," ","i","s"," ","s","k","y"," ","t","h","e"]
 *
 * 注意：
 *
 *
 * 单词的定义是不包含空格的一系列字符
 * 输入字符串中不会包含前置或尾随的空格
 * 单词与单词之间永远是以单个空格隔开的
 *
 *
 * 进阶：使用 O(1) 额外空间复杂度的原地解法。
 *
 */

export
// @lc code=start
function reverseWords(s: string[]): void {
  let begin = 0
  for (let i = 0; i < s.length; i++) {
    if (i === 0 || s[i - 1] === ' ') {
      begin = i
    }

    if (i === s.length - 1 || s[i + 1] === ' ') {
      reverse(s, begin, i)
    }
  }

  reverse(s, 0, s.length - 1)
}

function reverse(arr: any[], begin: number, end: number) {
  let i = begin, j = end

  while (i < j) {
    swap(arr, i++, j--)
  }
}

function swap(arr: any[], i: number, j: number) {
  const temp = arr[i]
  arr[i] = arr[j]
  arr[j] = temp
}
// @lc code=end
