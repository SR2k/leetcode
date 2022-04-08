/*
 * @lc app=leetcode.cn id=28 lang=typescript
 *
 * [28] 实现 strStr()
 *
 * https://leetcode-cn.com/problems/implement-strstr/description/
 *
 * algorithms
 * Easy (40.28%)
 * Likes:    1263
 * Dislikes: 0
 * Total Accepted:    562.1K
 * Total Submissions: 1.4M
 * Testcase Example:  '"hello"\n"ll"'
 *
 * 实现 strStr() 函数。
 *
 * 给你两个字符串 haystack 和 needle ，请你在 haystack 字符串中找出 needle 字符串出现的第一个位置（下标从 0
 * 开始）。如果不存在，则返回  -1 。
 *
 *
 *
 * 说明：
 *
 * 当 needle 是空字符串时，我们应当返回什么值呢？这是一个在面试中很好的问题。
 *
 * 对于本题而言，当 needle 是空字符串时我们应当返回 0 。这与 C 语言的 strstr() 以及 Java 的 indexOf()
 * 定义相符。
 *
 *
 *
 * 示例 1：
 *
 *
 * 输入：haystack = "hello", needle = "ll"
 * 输出：2
 *
 *
 * 示例 2：
 *
 *
 * 输入：haystack = "aaaaa", needle = "bba"
 * 输出：-1
 *
 *
 * 示例 3：
 *
 *
 * 输入：haystack = "", needle = ""
 * 输出：0
 *
 *
 *
 *
 * 提示：
 *
 *
 * 0
 * haystack 和 needle 仅由小写英文字符组成
 *
 *
 */

export
// @lc code=start
function strStr(haystack: string, needle: string): number {
  if (!needle) return 0
  if (!haystack) return -1
  if (needle.length > haystack.length) return -1

  const hashP = hash(needle)
  let hashS = hash(haystack, 0, needle.length - 1)

  if (hashS === hashP && check(needle, haystack, needle.length - 1)) {
    return 0
  }

  const TOP_SCALE = new Array(needle.length - 1)
    .fill(0)
    .reduce((prev) => (prev * SCALE) % MODULO, 1)

  for (let i = needle.length; i < haystack.length; i++) {
    const prev = i - needle.length
    hashS -= (haystack.charCodeAt(prev) * TOP_SCALE) % MODULO
    hashS += MODULO
    hashS %= MODULO
    hashS *= SCALE
    hashS %= MODULO
    hashS += haystack.charCodeAt(i)
    hashS %= MODULO

    if (hashS === hashP && check(needle, haystack, i)) {
      return prev + 1
    }
  }

  return -1
}

const SCALE = 31
const MODULO = 1e7

function hash(str: string, left = 0, right = str.length - 1) {
  let result = 0

  for (let i = left; i <= right; i++) {
    result *= SCALE
    result += str.charCodeAt(i)
    result %= MODULO
  }

  return result
}

function check(p: string, s: string, sEnd: number) {
  return p === s.slice(sEnd - p.length + 1, sEnd + 1)
}
// @lc code=end
