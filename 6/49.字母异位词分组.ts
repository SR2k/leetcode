/*
 * @lc app=leetcode.cn id=49 lang=typescript
 *
 * [49] 字母异位词分组
 *
 * https://leetcode.cn/problems/group-anagrams/description/
 *
 * algorithms
 * Medium (67.34%)
 * Likes:    1174
 * Dislikes: 0
 * Total Accepted:    343.8K
 * Total Submissions: 510.1K
 * Testcase Example:  '["eat","tea","tan","ate","nat","bat"]'
 *
 * 给你一个字符串数组，请你将 字母异位词 组合在一起。可以按任意顺序返回结果列表。
 *
 * 字母异位词 是由重新排列源单词的字母得到的一个新单词，所有源单词中的字母通常恰好只用一次。
 *
 *
 *
 * 示例 1:
 *
 *
 * 输入: strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
 * 输出: [["bat"],["nat","tan"],["ate","eat","tea"]]
 *
 * 示例 2:
 *
 *
 * 输入: strs = [""]
 * 输出: [[""]]
 *
 *
 * 示例 3:
 *
 *
 * 输入: strs = ["a"]
 * 输出: [["a"]]
 *
 *
 *
 * 提示：
 *
 *
 * 1 <= strs.length <= 10^4
 * 0 <= strs[i].length <= 100
 * strs[i] 仅包含小写字母
 *
 *
 */

export
// @lc code=start
function groupAnagrams(strs: string[]): string[][] {
  const mapping: Record<string, string[]> = {}
  strs.forEach((s) => {
    const h = hash(s)
    if (!mapping[h]) mapping[h] = []
    mapping[h].push(s)
  })
  return Object.values(mapping)
}

const CHAR_CODE_SMALL_A = 'a'.charCodeAt(0)

function hash(str: string) {
  const result = new Array<number>(26).fill(0)
  for (let i = 0; i < str.length; i++) {
    result[str.charCodeAt(i) - CHAR_CODE_SMALL_A]++
  }
  return result.join(',')
}
// @lc code=end
