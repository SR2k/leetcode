/*
 * @lc app=leetcode.cn id=140 lang=typescript
 *
 * [140] 单词拆分 II
 *
 * https://leetcode-cn.com/problems/word-break-ii/description/
 *
 * algorithms
 * Hard (51.11%)
 * Likes:    564
 * Dislikes: 0
 * Total Accepted:    61.1K
 * Total Submissions: 119.3K
 * Testcase Example:  '"catsanddog"\n["cat","cats","and","sand","dog"]'
 *
 * 给定一个字符串 s 和一个字符串字典 wordDict ，在字符串 s 中增加空格来构建一个句子，使得句子中所有的单词都在词典中。以任意顺序
 * 返回所有这些可能的句子。
 *
 * 注意：词典中的同一个单词可能在分段中被重复使用多次。
 *
 *
 *
 * 示例 1：
 *
 *
 * 输入:s = "catsanddog", wordDict = ["cat","cats","and","sand","dog"]
 * 输出:["cats and dog","cat sand dog"]
 *
 *
 * 示例 2：
 *
 *
 * 输入:s = "pineapplepenapple", wordDict =
 * ["apple","pen","applepen","pine","pineapple"]
 * 输出:["pine apple pen apple","pineapple pen apple","pine applepen apple"]
 * 解释: 注意你可以重复使用字典中的单词。
 *
 *
 * 示例 3：
 *
 *
 * 输入:s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
 * 输出:[]
 *
 *
 *
 *
 * 提示：
 *
 *
 *
 *
 * 1 <= s.length <= 20
 * 1 <= wordDict.length <= 1000
 * 1 <= wordDict[i].length <= 10
 * s 和 wordDict[i] 仅有小写英文字母组成
 * wordDict 中所有字符串都 不同
 *
 *
 */

export
// @lc code=start
function wordBreak(s: string, wordDict: string[]): string[] {
  const trie = buildTrie(wordDict)
  const result: string[] = []

  function helper(prev: string[], i: number) {
    if (i >= s.length) {
      result.push(prev.join(' '))
      return
    }

    for (const m of getMatched(s, i, trie)) {
      prev.push(m)
      helper(prev, i + m.length)
      prev.pop()
    }
  }
  helper([], 0)

  return result
}

/**
 * 从 str 的第 i 位开始，找到所有可以匹配上的单词
 */
function* getMatched(str: string, i: number, trie: Trie) {
  let curr = trie
  while (i < str.length) {
    curr = curr[str[i]]

    // 当前字符不在前缀树中，直接结束迭代
    if (!curr) return

    // 当前字符是某个单词的结尾，返回该结果
    if (curr['#']) {
      yield curr['#']
    }

    i += 1
  }
}

/**
 * 构建前缀树
 */
function buildTrie(words: string[]): Trie {
  const root: Trie = {}

  for (const word of words) {
    let curr = root

    for (const char of word) {
      if (!curr[char]) {
        curr[char] = {}
      }
      curr = curr[char]
    }

    curr['#'] = word
  }

  return root
}

type Trie = {
  [key: string]: Trie
} & {
  '#'?: string
}
// @lc code=end
