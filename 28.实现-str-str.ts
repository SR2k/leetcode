/*
 * @lc app=leetcode.cn id=28 lang=typescript
 *
 * [28] 实现 strStr()
 *
 * https://leetcode.cn/problems/implement-strstr/description/
 *
 * algorithms
 * Easy (41.28%)
 * Likes:    1562
 * Dislikes: 0
 * Total Accepted:    718.3K
 * Total Submissions: 1.7M
 * Testcase Example:  '"hello"\n"ll"'
 *
 * 实现 strStr() 函数。
 *
 * 给你两个字符串 haystack 和 needle ，请你在 haystack 字符串中找出 needle 字符串出现的第一个位置（下标从 0
 * 开始）。如果不存在，则返回  -1 。
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
 *
 *
 * 提示：
 *
 *
 * 1 <= haystack.length, needle.length <= 10^4
 * haystack 和 needle 仅由小写英文字符组成
 *
 *
 */

export
// @lc code=start
function strStr(haystack: string, needle: string): number {
  if (haystack.length < needle.length) {
    return -1
  }

  let needleHash = 0
  for (let i = 0; i < needle.length; i++) {
    needleHash = append2Hash(needleHash, needle[i])
  }

  let topScale = 1
  for (let i = 0; i < needle.length - 1; i++) {
    topScale = (topScale * SCALE) % MODULO
  }

  let hash = 0
  for (let i = 0; i < haystack.length; i++) {
    const prevBegin = i - needle.length

    if (prevBegin >= 0) {
      const removal = haystack.charCodeAt(prevBegin) - CHAR_CODE_SMALL_A
      hash -= removal * topScale
      hash = ((hash % MODULO) + MODULO) % MODULO
    }
    hash = append2Hash(hash, haystack[i])

    if (hash === needleHash && check(haystack, needle, i)) {
      return prevBegin + 1
    }
  }

  return -1
}

const SCALE = 31
const MODULO = 6e7

const CHAR_CODE_SMALL_A = 'a'.charCodeAt(0)

function append2Hash(currHash: number, adding: string) {
  let resultHash = currHash

  resultHash = resultHash * SCALE + adding.charCodeAt(0) - CHAR_CODE_SMALL_A
  resultHash %= MODULO

  return resultHash
}

function check(s: string, p: string, end: number) {
  for (let i = 0; i < p.length; i++) {
    if (s[end - i] !== p.at(-i - 1)) {
      return false
    }
  }
  return true
}
// @lc code=end
