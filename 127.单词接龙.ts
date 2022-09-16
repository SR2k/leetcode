/*
 * @lc app=leetcode.cn id=127 lang=typescript
 *
 * [127] 单词接龙
 *
 * https://leetcode.cn/problems/word-ladder/description/
 *
 * algorithms
 * Hard (47.97%)
 * Likes:    1133
 * Dislikes: 0
 * Total Accepted:    165.9K
 * Total Submissions: 345.7K
 * Testcase Example:  '"hit"\n"cog"\n["hot","dot","dog","lot","log","cog"]'
 *
 * 字典 wordList 中从单词 beginWord 和 endWord 的 转换序列 是一个按下述规格形成的序列 beginWord -> s1 ->
 * s2 -> ... -> sk：
 *
 *
 * 每一对相邻的单词只差一个字母。
 * 对于 1 <= i <= k 时，每个 si 都在 wordList 中。注意， beginWord 不需要在 wordList 中。
 * sk == endWord
 *
 *
 * 给你两个单词 beginWord 和 endWord 和一个字典 wordList ，返回 从 beginWord 到 endWord 的 最短转换序列
 * 中的 单词数目 。如果不存在这样的转换序列，返回 0 。
 *
 *
 * 示例 1：
 *
 *
 * 输入：beginWord = "hit", endWord = "cog", wordList =
 * ["hot","dot","dog","lot","log","cog"]
 * 输出：5
 * 解释：一个最短转换序列是 "hit" -> "hot" -> "dot" -> "dog" -> "cog", 返回它的长度 5。
 *
 *
 * 示例 2：
 *
 *
 * 输入：beginWord = "hit", endWord = "cog", wordList =
 * ["hot","dot","dog","lot","log"]
 * 输出：0
 * 解释：endWord "cog" 不在字典中，所以无法进行转换。
 *
 *
 *
 * 提示：
 *
 *
 * 1 <= beginWord.length <= 10
 * endWord.length == beginWord.length
 * 1 <= wordList.length <= 5000
 * wordList[i].length == beginWord.length
 * beginWord、endWord 和 wordList[i] 由小写英文字母组成
 * beginWord != endWord
 * wordList 中的所有字符串 互不相同
 *
 *
 */

export
// @lc code=start
function ladderLength(beginWord: string, endWord: string, wordList: string[]): number {
  const graph = buildGraph([beginWord, ...wordList])
  if (!graph[endWord]?.size) return 0

  const frontQueue = [beginWord]
  const frontSteps = new Map<string, number>()

  const endQueue = [endWord]
  const endSteps = new Map<string, number>()

  let frontCount = 0
  let endCount = 0

  while (frontQueue.length || endQueue.length) {
    while (frontQueue.length) {
      frontCount++

      const levelLength = frontQueue.length
      for (let i = 0; i < levelLength; i++) {
        const word = frontQueue.shift()!

        if (endSteps.has(word)) {
          return frontCount + endSteps.get(word)!
        }

        for (const next of graph[word]) {
          if (!frontSteps.has(next)) {
            frontSteps.set(next, frontCount)
            frontQueue.push(next)
          }
        }
      }
    }

    while (endQueue.length) {
      endCount++

      const levelLength = endQueue.length
      for (let i = 0; i < levelLength; i++) {
        const word = endQueue.shift()!

        if (frontSteps.has(word)) {
          return endCount + frontSteps.get(word)!
        }

        for (const next of graph[word]) {
          if (!endSteps.has(next)) {
            endSteps.set(next, endCount)
            endQueue.push(next)
          }
        }
      }
    }
  }

  return 0
}

function buildGraph(wordList: string[]) {
  const hash2Words: Record<string, Set<string>> = {}
  const word2Hash: Record<string, Set<string>> = {}

  for (const word of wordList) {
    word2Hash[word] = new Set()

    for (const hash of getHashes(word)) {
      hash2Words[hash] = hash2Words[hash] || new Set()
      hash2Words[hash].add(word)
      word2Hash[word].add(hash)
    }
  }

  const result: Record<string, Set<string>> = {}
  for (const word of wordList) {
    result[word] = new Set()
    for (const hash of word2Hash[word]) {
      for (const n of hash2Words[hash]) {
        result[word].add(n)
      }
    }
    result[word].delete(word)
  }

  return result
}

function getHashes(word: string) {
  const result: string[] = []
  for (let i = 0; i < word.length; i++) {
    result.push(`${word.slice(0, i)}?${word.slice(i + 1, word.length)}`)
  }
  return result
}
// @lc code=end

export {}
