/*
 * @lc app=leetcode.cn id=49 lang=typescript
 *
 * [49] 字母异位词分组
 *
 * https://leetcode.cn/problems/group-anagrams/description/
 *
 * algorithms
 * Medium (67.30%)
 * Likes:    1153
 * Dislikes: 0
 * Total Accepted:    330.9K
 * Total Submissions: 491.7K
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
  const hash2strs: Record<string, string[]> = {}
  strs.forEach(x => {
    const h = hash(x)
    if (!hash2strs[h]) {
      hash2strs[h] = [x]
    } else {
      hash2strs[h].push(x)
    }
  })
  return Object.values(hash2strs)
}

const CHAR_CODE_SMALL_A = 'a'.charCodeAt(0)

const getCharCodeIndex = (str: string, i: number) => str.charCodeAt(i) - CHAR_CODE_SMALL_A

const hash = (str: string) => {
  const counter = new Array<number>(26).fill(0)

  for (let i = 0; i < str.length; i++) {
    counter[getCharCodeIndex(str, i)]++
  }

  return counter.join(',')
}
// @lc code=end
