/*
 * @lc app=leetcode.cn id=127 lang=typescript
 *
 * [127] 单词接龙
 *
 * https://leetcode-cn.com/problems/word-ladder/description/
 *
 * algorithms
 * Hard (47.26%)
 * Likes:    958
 * Dislikes: 0
 * Total Accepted:    137.1K
 * Total Submissions: 290.1K
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
  const children: Record<string, string[]> = {}
  for (let i = 0; i < wordList.length - 1; i++) {
    const a = wordList[i]
    for (let j = i + 1; j < wordList.length; j++) {
      const b = wordList[j]
      if (check(a, b)) {
        ensure(children, a).push(b)
        ensure(children, b).push(a)
      }
    }
  }
  if (!children[beginWord]) {
    for (let j = 0; j < wordList.length; j++) {
      const b = wordList[j]
      if (check(beginWord, b)) {
        ensure(children, beginWord).push(b)
      }
    }
  }

  const queue = [beginWord]
  const seen = new Set(queue)
  let result = 0
  while (queue.length) {
    const levelLength = queue.length
    result += 1

    for (let i = 0; i < levelLength; i++) {
      const word = queue.shift()!;

      for (const child of children[word] || []) {
        if (child === endWord) {
          return result + 1
        }
        if (seen.has(child)) continue
        seen.add(child)
        queue.push(child)
      }
    }
  }

  return 0
}

function check(a: string, b: string) {
  let diffCount = 0
  for (let i = 0; i < a.length; i++) {
    if (a[i] !== b[i]) {
      diffCount++
    }
    if (diffCount > 1) return false
  }
  return true
}

function ensure(map: Record<string, string[]>, key: string) {
  if (!map[key]) map[key] = []
  return map[key]
}
// @lc code=end
