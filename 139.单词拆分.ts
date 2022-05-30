/*
 * @lc app=leetcode.cn id=139 lang=typescript
 *
 * [139] 单词拆分
 *
 * https://leetcode.cn/problems/word-break/description/
 *
 * algorithms
 * Medium (53.00%)
 * Likes:    1609
 * Dislikes: 0
 * Total Accepted:    297.6K
 * Total Submissions: 560.6K
 * Testcase Example:  '"leetcode"\n["leet","code"]'
 *
 * 给你一个字符串 s 和一个字符串列表 wordDict 作为字典。请你判断是否可以利用字典中出现的单词拼接出 s 。
 *
 * 注意：不要求字典中出现的单词全部都使用，并且字典中的单词可以重复使用。
 *
 *
 *
 * 示例 1：
 *
 *
 * 输入: s = "leetcode", wordDict = ["leet", "code"]
 * 输出: true
 * 解释: 返回 true 因为 "leetcode" 可以由 "leet" 和 "code" 拼接成。
 *
 *
 * 示例 2：
 *
 *
 * 输入: s = "applepenapple", wordDict = ["apple", "pen"]
 * 输出: true
 * 解释: 返回 true 因为 "applepenapple" 可以由 "apple" "pen" "apple" 拼接成。
 * 注意，你可以重复使用字典中的单词。
 *
 *
 * 示例 3：
 *
 *
 * 输入: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
 * 输出: false
 *
 *
 *
 *
 * 提示：
 *
 *
 * 1 <= s.length <= 300
 * 1 <= wordDict.length <= 1000
 * 1 <= wordDict[i].length <= 20
 * s 和 wordDict[i] 仅有小写英文字母组成
 * wordDict 中的所有字符串 互不相同
 *
 *
 */

// @lc code=start
type TrieNode = {
  [key: string]: TrieNode
} & {
  end?: boolean
}

class Trie {
  root: TrieNode = {}

  height = 0

  add(word: string) {
    let curr = this.root
    let currHeight = 0

    for (let i = 0; i < word.length; i++) {
      if (!curr[word[i]]) {
        curr[word[i]] = {}
      }
      curr = curr[word[i]]
      currHeight += 1
    }

    curr.end = true
    this.height = Math.max(this.height, currHeight)
  }
}

function wordBreak(s: string, wordDict: string[]): boolean {
  const trie = new Trie()
  wordDict.forEach((x) => trie.add(x))

  const cache: Record<number, boolean> = {}
  const withCache = (fn: (i: number) => boolean) => (i: number) => {
    if (typeof cache[i] !== 'boolean') {
      cache[i] = fn(i)
    }
    return cache[i]
  }

  const helper = withCache((i: number) => {
    if (i === s.length) {
      return true
    }

    let curr = trie.root
    while (curr && i < s.length) {
      const char = s[i]
      if (!curr[char]) {
        return false
      }

      curr = curr[char]
      if (curr.end && helper(i + 1)) {
        return true
      }

      i += 1
    }

    return false
  })

  return helper(0)
}
// @lc code=end

console.log(wordBreak('applepenapple', ['apple', 'pen']))
console.log(wordBreak('catsandog', ['cats', 'dog', 'sand', 'and', 'cat']))
console.log(wordBreak('c', ['cats', 'dog', 'sand', 'and', 'cat']))
console.log(wordBreak('c', ['c']))
